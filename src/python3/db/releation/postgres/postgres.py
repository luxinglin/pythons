# -* - coding: UTF-8 -* -

import psycopg2

from excel.excelWrite import export_to_excel

# 创建连接对象
conn = psycopg2.connect(database="dcsm-1026", user="postgres", password="!qaz2wsx3edc", host="localhost", port="5432")

# 创建指针对象
cur = conn.cursor()

# 查询表头
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name ='sys_code_items';")
headers = cur.fetchall()

# 查询数据
cur.execute('SELECT * FROM sys_code_items;')
results = cur.fetchall()

data_list = []
data_list.append(headers)
for item in results:
    data_list.append(item)

export_to_excel(data_list, "code_items.xls")

# 关闭链接
conn.commit()
cur.close()
conn.close()
