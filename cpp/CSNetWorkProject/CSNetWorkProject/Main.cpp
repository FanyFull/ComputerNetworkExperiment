#define _CRT_SECURE_NO_WARNINGS
#include <pcap.h>
#include <Winsock2.h>
#include <time.h>
#include <tchar.h>
#include<stdlib.h>
#include "DBMySQL.h"
#include<string>
#include<iostream>


// 加载 npcap 的 dll
BOOL LoadNpcapDlls()
{
    _TCHAR npcap_dir[512];
    UINT len;
    len = GetSystemDirectory(npcap_dir, 480);
    if (!len) {
        fprintf(stderr, "Error in GetSystemDirectory: %x", GetLastError());
        return FALSE;
    }
    _tcscat_s(npcap_dir, 512, _T("\\Npcap"));
    if (SetDllDirectory(npcap_dir) == 0) {
        fprintf(stderr, "Error in SetDllDirectory: %x", GetLastError());
        return FALSE;
    }
    return TRUE;
}


/* 4 bytes IP address */
typedef struct ip_address {
    u_char byte1;
    u_char byte2;
    u_char byte3;
    u_char byte4;
}ip_address;

/* IPv4 header */
typedef struct ip_header {
    u_char  ver_ihl; // Version (4 bits) + IP header length (4 bits)
    u_char  tos;     // Type of service 
    u_short tlen;    // Total length 
    u_short identification; // Identification
    u_short flags_fo; // Flags (3 bits) + Fragment offset (13 bits)
    u_char  ttl;      // Time to live
    u_char  proto;    // Protocol
    u_short crc;      // Header checksum
    ip_address  saddr; // Source address
    ip_address  daddr; // Destination address
    u_int  op_pad;     // Option + Padding
}ip_header;

/* UDP header*/
typedef struct udp_header {
    u_short sport; // Source port
    u_short dport; // Destination port
    u_short len;   // Datagram length
    u_short crc;   // Checksum
}udp_header;

/* prototype of the packet handler */
void packet_handler(u_char* param,
    const struct pcap_pkthdr* header,
    const u_char* pkt_data);

VspdCToMySQL* vspdctomysql = NULL;
int id = 0; // 作为数据库表中的 id

int main()
{
    // 初始化 pcap
    pcap_if_t* alldevs;
    pcap_if_t* d;
    int inum;
    int i = 0;
    pcap_t* adhandle;
    char errbuf[PCAP_ERRBUF_SIZE];
    u_int netmask;
    char packet_filter[] = "ip and tcp";
    struct bpf_program fcode;

    // 初始化数据库相关
    printf("开始连接数据库\n");
    char host[] = "127.0.0.1";
    char user[] = "root";
    char port[] = "3306";
    char passwd[] = "lf123456";
    char dbname[] = "computer_network";
    char charset[] = "utf8"; // 设置字符集为 UTF-8
    char Msg[] = ""; // 消息变量
    // 初始化
    vspdctomysql = new VspdCToMySQL;
    int res = vspdctomysql->ConnMySQL(host, port, dbname, user, passwd, charset, Msg);
    if (res == 0)
        printf("MySQL connect success\n");
    else
        printf(Msg);

    // 查询
    const char* SQL = "SELECT id, src_ip, dst_ip FROM test_tb";
    string str = vspdctomysql->SelectData(SQL, 3, Msg);
    if (str.length() > 0)
    {
        printf("select success\n");
        //printf(str.data());
        printf("\n");
    }
    else
    {
        printf(Msg);
    }

    // 先清空上一次抓包保存的数据
    SQL = "delete from test_tb where 1 = 1";
    if (vspdctomysql->DeleteData(SQL, Msg) == 0)
        printf("delete success\n");


    /* Load Npcap and its functions. */
    if (!LoadNpcapDlls())
    {
        fprintf(stderr, "Couldn't load Npcap\n");
        exit(1);
    }

    /* Retrieve the device list */
    if (pcap_findalldevs_ex(PCAP_SRC_IF_STRING,
        NULL, &alldevs, errbuf) == -1)
    {
        fprintf(stderr, "Error in pcap_findalldevs: %s\n", errbuf);
        exit(1);
    }

    /* Print the list */
    for (d = alldevs; d; d = d->next)
    {
        printf("%d. %s", ++i, d->name);
        if (d->description)
            printf(" (%s)\n", d->description);
        else
            printf(" (No description available)\n");
    }

    if (i == 0)
    {
        printf("\nNo interfaces found! Make sure Npcap is installed.\n");
        return -1;
    }

    printf("Enter the interface number (1-%d):", i);
    scanf_s("%d", &inum);

    if (inum < 1 || inum > i)
    {
        printf("\nInterface number out of range.\n");
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    /* Jump to the selected adapter */
    for (d = alldevs, i = 0; i < inum - 1;d = d->next, i++);

    /* Open the adapter */
    if ((adhandle = pcap_open(d->name, // name of the device
        65536, // portion of the packet to capture. 
               // 65536 grants that the whole packet
               // will be captured on all the MACs.
        PCAP_OPENFLAG_PROMISCUOUS, // promiscuous mode
        1000, // read timeout
        NULL, // remote authentication
        errbuf // error buffer
    )) == NULL)
    {
        fprintf(stderr,
            "\nUnable to open the adapter. %s is not supported by Npcap\n",
            d->name);
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    /* Check the link layer. We support only Ethernet for simplicity. */
    if (pcap_datalink(adhandle) != DLT_EN10MB)
    {
        fprintf(stderr, "\nThis program works only on Ethernet networks.\n");
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    if (d->addresses != NULL)
        /* Retrieve the mask of the first address of the interface */
        netmask = ((struct sockaddr_in*)(d->addresses->netmask))->sin_addr.S_un.S_addr;
    else
        /* If the interface is without addresses
         * we suppose to be in a C class network */
        netmask = 0xffffff;


    //compile the filter
    if (pcap_compile(adhandle, &fcode, packet_filter, 1, netmask) < 0)
    {
        fprintf(stderr, "\nUnable to compile the packet filter. Check the syntax.\n");
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    //set the filter
    if (pcap_setfilter(adhandle, &fcode) < 0)
    {
        fprintf(stderr, "\nError setting the filter.\n");
        /* Free the device list */
        pcap_freealldevs(alldevs);
        return -1;
    }

    printf("\nlistening on %s...\n", d->description);

    /* At this point, we don't need any more the device list. Free it */
    pcap_freealldevs(alldevs);

    /* start the capture */
    pcap_loop(adhandle, 0, packet_handler, NULL);

    // 用完之后关闭数据库的连接
    vspdctomysql->CloseMySQLConn();
    printf("结束连接数据库\n");

    return 0;
}

/* Callback function invoked by libpcap for every incoming packet */
void packet_handler(u_char* param,
    const struct pcap_pkthdr* header,
    const u_char* pkt_data)
{
    struct tm ltime;
    char timestr[16];
    ip_header* ih;
    udp_header* uh;
    u_int ip_len;
    u_short sport, dport;
    time_t local_tv_sec;

    /*
     * Unused variable
     */
    (VOID)(param);

    /* convert the timestamp to readable format */
    local_tv_sec = header->ts.tv_sec;
    localtime_s(&ltime, &local_tv_sec);
    strftime(timestr, sizeof timestr, "%H:%M:%S", &ltime);

    /* print timestamp and length of the packet */
    printf("%s.%.6d len:%d ", timestr, header->ts.tv_usec, header->len);

    /* retireve the position of the ip header */
    ih = (ip_header*)(pkt_data +
        14); //length of ethernet header

      /* retireve the position of the udp header */
    ip_len = (ih->ver_ihl & 0xf) * 4;
    uh = (udp_header*)((u_char*)ih + ip_len);

    /* convert from network byte order to host byte order */
    sport = ntohs(uh->sport);
    dport = ntohs(uh->dport);

    /* print ip addresses and udp ports */
    printf("%d.%d.%d.%d.%d -> %d.%d.%d.%d.%d\n",
        ih->saddr.byte1,
        ih->saddr.byte2,
        ih->saddr.byte3,
        ih->saddr.byte4,
        sport,
        ih->daddr.byte1,
        ih->daddr.byte2,
        ih->daddr.byte3,
        ih->daddr.byte4,
        dport);

    // 将源 ip 地址和目的 ip 地址转换成字符串
    string srcIp = to_string(ih->saddr.byte1) + "." + to_string(ih->saddr.byte2) + "." + to_string(ih->saddr.byte3) + "." + to_string(ih->saddr.byte4);
    string dstIp = to_string(ih->daddr.byte1) + "." + to_string(ih->daddr.byte2) + "." + to_string(ih->daddr.byte3) + "." + to_string(ih->daddr.byte4);
    cout << "src ip  " << srcIp << "\t" << endl;
    cout << "dst ip  " << dstIp << "\t" << endl;
    cout << "=========" << endl;
    string SQLString = "insert into test_tb(id, src_ip, dst_ip) values(" + to_string(++id) + ", '" + srcIp + "', "
        + "'" + dstIp + "')";
    cout << SQLString << endl;
    // 插入数据
    /*const char* SQL = "insert into test_tb(id, src_ip, dst_ip) values(4, 'qingxiaofeng', 'fsdajfjsad')";
    */
    const char* SQL = SQLString.c_str();
    const char* Msg = "";
    if (vspdctomysql->InsertData(SQL, Msg) == 0)
    {
        printf("insert success\n");
    }
}