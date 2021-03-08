"""
===============================
author: ghj
Time: 2020/6/18 9:50
Project: 数据库编程
File: handle_excel.py
================================
"""
# -_- coding=utf-8 -_-
from openpyxl import load_workbook



class HandleExcel:
    def __init__(self, file_path, sheet_name):
        # 获取工作簿绝对路径
        self.wb = load_workbook(file_path)
        # 根据表单获取表单名称
        self.sh = self.wb[sheet_name]

    def read_titles(self):
        titles = []
        # 遍历sheet第一行，得到title
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        # 取表单除了第一行的所有数据，遍历表单从第二行开始所有的单元格
        # 会得到由每行单元格元祖构成的单元格列表，遍历列表得到每行的单元格
        for item in list(self.sh.rows)[1:]:
            titles = self.read_titles()
            values = []
            # 遍历每行单元格，会得到每个单元格，单元格.value会得到每个单元格的值
            for val in item:
                values.append(val.value)
                # 用zip函数，将每行单元格的内容打包成字典
            res = dict(zip(titles, values))
            # eval函数将"check"的值，转换成字典对象
            res["check"] = eval(res["check"])
            all_datas.append(res)
        return all_datas

    def close_excel(self):
        self.wb.close()


if __name__ == '__main__':
    import os
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases_data111.xlsx")
    exc = HandleExcel(file_name, "login_case")
    all_datas=exc.read_all_datas()
    print(all_datas)
