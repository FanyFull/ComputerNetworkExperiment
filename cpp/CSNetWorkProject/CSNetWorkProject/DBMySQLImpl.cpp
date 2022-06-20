//#include "stdafx.h"
#include "DBMySQL.h"

VspdCToMySQL::VspdCToMySQL()
{
}

VspdCToMySQL::~VspdCToMySQL()
{
}

//��ʼ������
int VspdCToMySQL::ConnMySQL(const char* host, const char* port, const char* Db, const char* user, const char* passwd, const char* const charset, const char* Msg)
{
	if (mysql_init(&mysql) == NULL)
	{
		Msg = "inital mysql handle error";
		return 1;
	}

	if (mysql_real_connect(&mysql, host, user, passwd, Db, 0, NULL, 0) == NULL)
	{
		Msg = "Failed to connect to database: Error";
		return 1;
	}

	if (mysql_set_character_set(&mysql, charset) != 0)
	{
		Msg = "mysql_set_character_set Error";
		return 1;
	}
	return 0;
}

//��ѯ����
string VspdCToMySQL::SelectData(const char* SQL, int Cnum, const char* Msg)
{
	MYSQL_ROW m_row;
	MYSQL_RES* m_res;
	char sql[2048];
	sprintf(sql, SQL);
	int rnum = 0;
	char rg = '\n';//�и���
	// char rg='\r';
	char cg = '\t';//�ֶθ���
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "select ps_info Error";
		return "";
	}
	m_res = mysql_store_result(&mysql);

	if (m_res == NULL)
	{
		Msg = "select username Error";
		return "";
	}
	string str("");
	while (m_row = mysql_fetch_row(m_res))
	{
		for (int i = 0; i < Cnum; i++)
		{
			str += m_row[i];
			str += cg;
		}
		str += rg;
		rnum++;
	}

	mysql_free_result(m_res);

	return str;
}

//��������
int VspdCToMySQL::InsertData(const char* SQL, const char* Msg)
{
	char sql[2048];
	sprintf(sql, SQL);
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "Insert Data Error";
		return 1;
	}
	return 0;
}

//��������
int VspdCToMySQL::ReplaceData(const char* SQL, const char* Msg)
{
	char sql[2048];
	sprintf(sql, SQL);
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "Replace Data Error";
		return 1;
	}
	return 0;
}

//��������
int VspdCToMySQL::UpdateData(const char* SQL, const char* Msg)
{
	char sql[2048];
	sprintf(sql, SQL);
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "Update Data Error";
		return 1;
	}
	return 0;
}

//ɾ������
int VspdCToMySQL::DeleteData(const char* SQL, const char* Msg)
{
	char sql[2048];
	sprintf(sql, SQL);
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "Delete Data error";
		return 1;
	}
	return 0;
}

//�������ݿ�洢����
int VspdCToMySQL::CallProcedure(const char* SQL, const char* Msg)
{
	char sql[2048];
	sprintf(sql, SQL);
	if (mysql_query(&mysql, sql) != 0)
	{
		Msg = "Call Procedure error";
		return 1;
	}
	return 0;
}
//�ر����ݿ�����
void VspdCToMySQL::CloseMySQLConn()
{
	mysql_close(&mysql);
	printf("disconnect database\n");
}