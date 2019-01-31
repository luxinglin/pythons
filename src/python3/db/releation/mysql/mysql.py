# -* - coding: UTF-8 -* -  

import pymysql

from excel.excelWrite import export_to_excel

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "dcim-saas-dev")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)

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

# 关闭数据库连接
cursor.close()
db.close()
