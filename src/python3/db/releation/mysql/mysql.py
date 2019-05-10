# -* - coding: UTF-8 -* -  

import pymysql

from excel.excelWrite import export_to_excel

# def __init__(self, host=None, user=None, password="",
#                  database=None, port=0, unix_socket=None,
#              ;

conn = {
    'host': '10.200.132.160',
    # 'host': '10.200.131.51',
    'user': 'root',
    'password': 'Pioneer@2017',
    'database': 'dcim-saas-dev',
    # 'database': 'dcim-saas',
    'port': 3306
}
# 打开数据库连接
db = pymysql.connect(**conn)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def export_res_inst_2_excel():
    columns = []
    cursor.execute("describe res_inst;")
    defs = cursor.fetchall()
    for col_def in defs:
        columns.append(col_def[0])

    cursor.execute("select * from res_inst;")
    results = cursor.fetchall()

    result_list = []
    result_list.append(columns)
    for item in results:
        result_list.append(item)

    export_to_excel(result_list, "res_inst.xls")


def export_alerts_2_excel(cursor):
    column_headers = ["ALERT_ID", "COMPANY_ID", "ALERT_START_TIME", "ALERT_CONTENT"]

    alert_sql = "select t1.ALERT_ID,t1.COMPANY_ID,t1.ALERT_START_TIME,t1.ALERT_CONTENT " \
                " from (" \
                " select alert_id,COMPANY_ID,ALERT_START_TIME,ALERT_CONTENT from alert " \
                " union ALL " \
                " select alert_id,COMPANY_ID,ALERT_START_TIME,ALERT_CONTENT from alert_history " \
                " ) as t1 where t1.COMPANY_ID=16 order by COMPANY_ID asc, ALERT_START_TIME asc;"

    cursor.execute(alert_sql)
    results = cursor.fetchall()

    rows_list = []
    rows_list.append(column_headers)
    for result in results:
        rows_list.append(result)

    export_to_excel(rows_list, "all_alert.xls")


def select_data(sql):
    cursor.execute(sql)
    results = cursor.fetchall()

    return results


if __name__ == '__main__':
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    export_alerts_2_excel(cursor)

    # export_res_inst_2_excel(cursor)

    # 关闭数据库连接
    cursor.close()
    db.close()
