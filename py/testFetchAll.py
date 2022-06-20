from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_tb")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        res = set()
        for row in rows:
            if row[3] == None and row[4] == None:
                res.add(row)
        print(res)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchall()
