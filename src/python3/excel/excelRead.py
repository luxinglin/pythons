# -* - coding: UTF-8 -* -

import xlrd

# 只能读不能写
# 打开一个excel
book = xlrd.open_workbook('E:/stu_1.xls')
# 根据顺序获取sheet
sheet = book.sheet_by_index(0)
# 根据sheet页名字获取sheet
sheet2 = book.sheet_by_name('名单')
# 指定行和列获取数据
print(sheet.cell(0, 0).value)
print(sheet.cell(0, 1).value)
print(sheet.cell(0, 2).value)
print(sheet.cell(0, 3).value)
# 获取excel里面有多少列
print('列数：{0}'.format(sheet.ncols))
# 获取excel里面有多少行
print('行数：{0}'.format(sheet.nrows))
print(sheet.get_rows())
for i in sheet.get_rows():
    # 获取每一行的数据
    print(i)

# 0 1 2 3 4 5
for i in range(sheet.nrows):
    # 获取第几行的数据
    print(sheet.row_values(i))
# 取第一列的数据
print(sheet.col_values(1))
for i in range(sheet.ncols):
    # 获取第几列的数据
    print(sheet.col_values(i))
