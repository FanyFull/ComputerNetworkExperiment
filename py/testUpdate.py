import time
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import requests


def getJson(ip):
    myUrl = 'https://ip.useragentinfo.com/json?ip=' + ip
    # myUrl = 'http://whois.pconline.com.cn/ipJson.jsp?ip=' + ip + '&json=true'
    # ip = '40.79.150.121'
    r = requests.get(myUrl)
    return r.json()


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_tb")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        res = []
        for row in rows:
            if row[3] == None and row[4] == None:
                res.append(row)
        # print(res)
        return res
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def update_testTb():
    cityData = ["北京", "天津", "上海", "重庆", "石家庄", "唐山", "秦皇岛", "邯 郸",
                "邢台", "保定", "张家口", "承德", "沧州", "廊坊", "衡水", "太原", "大同",
                "阳泉", "长治", "晋城", "朔州", "晋中", "运城", "忻州", "临汾", "吕梁",
                "呼和浩特", "包头", "乌海", "赤峰", "通辽", "鄂尔多斯", "呼伦贝尔", "巴彦淖尔",
                "乌兰察布", "兴安", "锡林郭勒", "阿拉善", "沈阳", "大连", "鞍山", "抚顺",
                "本溪", "丹东", "锦州", "营口", "阜新", "辽阳", "盘锦", "铁岭", "朝阳",
                "葫芦岛", "长春", "吉林", "四平", "辽源", "通化", "白山", "松原", "白城",
                "延边朝鲜族自治", "哈尔滨", "齐齐哈尔", "鸡西", "鹤岗", "双鸭山", "大庆",
                "伊春", "佳木斯", "七台河", "牡丹江", "黑河", "绥化", "大兴安岭地", "南京",
                "无锡", "徐州", "常州", "苏州", "南通", "连云港", "淮安", "盐城", "扬州",
                "镇江", "泰州", "宿迁", "杭州", "宁波", "温州", "嘉兴", "湖州", "绍兴",
                "金华", "衢州", "舟山", "台州", "丽水", "合肥", "芜湖", "蚌埠", "淮南",
                "马鞍山", "淮北", "铜陵", "安庆", "黄山", "滁州", "阜阳", "宿州", "巢湖",
                "六安", "亳州", "池州", "宣城", "福州", "厦门", "莆田", "三明", "泉州",
                "漳州", "南平", "龙岩", "宁德", "南昌", "景德镇", "萍乡", "九江", "新余",
                "鹰潭", "赣州", "吉安", "宜春", "抚州", "上饶", "济南", "青岛", "淄博",
                "枣庄", "东营", "烟台", "潍坊", "济宁", "泰安", "威海", "日照", "莱芜",
                "临沂", "德州", "聊城", "滨州", "郑州", "开封", "洛阳", "平顶山", "安阳",
                "鹤壁", "新乡", "焦作", "濮阳", "许昌", "漯河", "三门峡", "南阳", "商丘",
                "信阳", "周口", "驻马店", "武汉", "黄石", "十堰", "宜昌", "襄樊", "鄂州",
                "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施土家族苗族自治", "长沙",
                "株洲", "湘潭", "衡阳", "邵阳", "岳阳", "常德", "张家界", "益阳", "郴州",
                "永州", "怀化", "娄底", "湘西土家族苗族自治", "广州", "韶关", "深圳", "珠海",
                "汕头", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾", "河源",
                "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮", "南宁", "柳州",
                "桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州",
                "河池", "来宾", "崇左", "海口", "三亚", "成都", "自贡", "攀枝花", "泸州",
                "德阳", "绵阳", "广元", "遂宁", "内江", "乐山", "南充", "眉山", "宜宾", "广安",
                "达州", "雅安", "巴中", "资阳", "阿坝藏族羌族自治", "甘孜藏族自治", "凉山彝族自治",
                "贵阳", "六盘水", "遵义", "安顺", "铜仁地", "黔西南布依族苗族自治", "毕节地",
                "黔东南苗族侗族自治", "黔南布依族苗族自治", "昆明", "曲靖", "玉溪", "保山",
                "昭通", "丽江", "临沧", "楚雄彝族自治", "红河哈尼族彝族自治", "文山壮族苗族自治",
                "西双版纳傣族自治", "大理白族自治", "德宏傣族景颇族自治", "怒江傈僳族自治",
                "迪庆藏族自治", "拉萨", "昌都地", "山南地", "日喀则地", "那曲地", "阿里地",
                "林芝地", "西安", "铜川", "宝鸡", "咸阳", "渭南", "延安", "汉中", "榆林",
                "安康", "商洛", "兰州", "嘉峪关", "金昌", "白银", "天水", "武威", "张掖",
                "平凉", "酒泉", "庆阳", "定西", "陇南", "临夏回族自治", "甘南藏族自治", "西宁",
                "海东地", "海北藏族自治", "黄南藏族自治", "海南藏族自治", "果洛藏族自治",
                "玉树藏族自治", "海西蒙古族藏族自治", "银川", "石嘴山", "吴忠", "固原", "中卫",
                "乌鲁木齐", "克拉玛依", "吐鲁番地", "哈密地", "昌吉回族自治", "博尔塔拉蒙古自治",
                "巴音郭楞蒙古自治", "阿克苏地", "克孜勒苏柯尔克孜自治", "喀什地", "和田地",
                "伊犁哈萨克自治", "塔城地", "阿勒泰地", "仙桃", "潜江", "天门", "神农架林",
                "五指山", "琼海", "儋州", "文昌", "万宁", "东方", "定安县", "屯昌县", "澄迈县",
                "临高县", "白沙黎族自治县", "昌江黎族自治县", "乐东黎族自治县", "陵水黎族自治县",
                "保亭黎族苗族自治县", "琼中黎族苗族自治县", "石河子"]
    # read database configuration
    db_config = read_db_config()

    toBeProcessedData = query_with_fetchall()

    # prepare query and data
    query = """ UPDATE test_tb
                SET src_loc = %s, dst_loc = %s
                WHERE id = %s """

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        # cursor.execute(query, data)

        for row in toBeProcessedData:
            rowId = row[0]
            srcIp = row[1]
            dstIp = row[2]

            if srcIp == '10.16.80.216': # 这里要替换成本机的 ip
                srcLoc = '武汉'
            else:
                srcJsonData = getJson(srcIp)
                print(srcJsonData)
                srcLoc = srcJsonData['city'][0:-1]
            time.sleep(1)
            if dstIp == '10.16.80.216': # 这里要替换成本机的 ip
                dstLoc = '武汉'
            else:
                dstJsonData = getJson(dstIp)
                dstLoc = dstJsonData['city'][0:-1]
            time.sleep(1)

            if srcLoc != '' and srcLoc not in cityData:
                srcLoc = '海外'
            if dstLoc != '' and dstLoc not in cityData:
                dstLoc = '海外'

            print(srcLoc + dstLoc)
            print(row)
            print('==========分割线=========')
            data = (srcLoc, dstLoc, rowId)
            cursor.execute(query, data)
            conn.commit()

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    while True:
        update_testTb()
