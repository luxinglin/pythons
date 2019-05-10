# -* - coding: UTF-8 -* -
import xlwt

_root_path_ = "E:/data/python/"


def export_to_excel(row_list, file_name):
    # 新建一个excel
    book = xlwt.Workbook()
    # 添加一个sheet页
    sheet = book.add_sheet('名单')
    # 控制行
    row = 0
    for row_item in row_list:
        # 控制列
        col = 0
        # 再循环里面list的值，每一列
        for cell_item in row_item:
            # if (typeof(cell_item)== "datetime")
            #     sheet.write(row, col, time.strptime(cell_item, "%Y-%m-%d %H:%M:%S"))
            # else
            sheet.write(row, col, cell_item)
            col += 1
        row += 1

    # 保存到当前目录下
    book.save(_root_path_ + file_name)


# 只能写不能读
students = [
    ['姓名', '年龄', '性别', '分数', '出生日期'],
    ['mary1', 20, '女', 89.9, '1988-01-02'],
    ['mary2', 20, '女', 89.9, '1988-01-03'],
    ['mary3', 20, '女', 89.9, '1988-01-04'],
    ['mary4', 20, '女', 89.9, '1988-01-05']
]

if __name__ == '__main__':
    export_to_excel(students, "student.xls")
