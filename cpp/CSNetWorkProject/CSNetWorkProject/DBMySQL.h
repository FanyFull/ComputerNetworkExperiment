#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
//#include <afxsock.h>
#include "mysql.h"

using namespace std;
class VspdCToMySQL
{
public:

	//����
	MYSQL mysql;

	/*
	���캯����ϡ������
	*/
	VspdCToMySQL();
	~VspdCToMySQL();

	/*
	��Ҫ�Ĺ��ܣ�
	��ʼ�����ݿ�
	�������ݿ�
	�����ַ���

	��ڲ�����
	host ��MYSQL������IP
	port:���ݿ�˿�
	Db�����ݿ�����
	user�����ݿ��û�
	passwd�����ݿ��û�������
	const charset��ϣ��ʹ�õ��ַ���
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	int ��0��ʾ�ɹ���1��ʾʧ��
	*/
	int ConnMySQL(const char* host, const char* port, const char* Db, const char* user, const char* passwd, const char* const charset, const char* Msg);

	/*
	��Ҫ�Ĺ��ܣ�
	��ѯ����

	��ڲ�����
	SQL����ѯ��SQL���
	Cnum:��ѯ������
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	string ׼�����÷��ص����ݣ�������¼����0x06����,�����λ��0x05����
	��� ���صĳ��ȣ� 0�����ʾ����
	*/
	string SelectData(const char* SQL, int Cnum, const char* Msg);

	/*
	��Ҫ���ܣ�
	��������

	��ڲ���
	SQL����ѯ��SQL���
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	int ��0��ʾ�ɹ���1��ʾʧ��
	*/
	int InsertData(const char* SQL, const char* Msg);

	/*
	��Ҫ���ܣ�
	��������ͬ��¼����������
	������ͬ��¼����������

	��ڲ���
	SQL����ѯ��SQL���
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	int ��0��ʾ�ɹ���1��ʾʧ��
	*/
	int ReplaceData(const char* SQL, const char* Msg);

	/*
	��Ҫ���ܣ�
	�޸�����

	��ڲ���
	SQL����ѯ��SQL���
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	int ��0��ʾ�ɹ���1��ʾʧ��
	*/
	int UpdateData(const char* SQL, const char* Msg);

	/*
	��Ҫ����:
	�������ݿ�洢����
	*/

	int CallProcedure(const char* SQL, const char* Msg);

	/*
	��Ҫ���ܣ�
	ɾ������

	��ڲ���
	SQL����ѯ��SQL���
	Msg:���ص���Ϣ������������Ϣ

	���ڲ�����
	int ��0��ʾ�ɹ���1��ʾʧ��
	*/
	int DeleteData(const char* SQL, const char* Msg);

	/*
	��Ҫ���ܣ�
	�ر����ݿ�����
	*/
	void CloseMySQLConn();

};