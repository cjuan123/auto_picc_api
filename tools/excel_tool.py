# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: excel_tool.py
@time: 2019/9/16 16:00
@desc：读取excel数据
"""
import os
import xlrd
from tools.path_tool import FilePath


class ReadExcel:
    def __init__(self, excel_path):
        self.file_path = FilePath().excel_path()
        self.path = os.path.join(self.file_path, excel_path)
        # 打开excel文件
        work_book = xlrd.open_workbook(self.path, encoding_override="utf-8")
        self.data_sheet = work_book.sheet_by_name("case")

    def row_num(self):
        """获取行数"""
        row_num = self.data_sheet.nrows  # 行数
        return int(row_num)

    def row_value(self, api_name):
        row_values = []
        for num in range(1, len(self.data_sheet.col_values(1))):
            if self.data_sheet.row_values(num)[1] == api_name:
                row_values.append(self.data_sheet.row_values(num))
        return row_values


# if __name__ == '__main__':
#     read = ReadExcel("case_data.xlsx").row_value("/web/department/add")
#     print(read)