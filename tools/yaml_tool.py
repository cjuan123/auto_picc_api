# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: yaml_tool.py
@time: 2019/9/16 14:59
@desc：读取yaml文件内容
"""
import yaml
import os
from tools.log_tool import Logger
from tools.path_tool import FilePath


class ReadYaml:
    def __init__(self, path):
        self.log = Logger()
        self.file_path = FilePath().conf_path()
        self.path = os.path.join(self.file_path, path)

    def open_yaml(self):
        """打开yaml文件"""
        try:
            with open(self.path, 'r', encoding='utf-8') as u:
                url_data = yaml.load(u, Loader=yaml.FullLoader)
            return url_data
        except Exception as e:
            self.log.error("【读取yaml文件错误】 - 【错误原因：%s】" % e)
        return url_data

    def get_host(self):
        """获取host值"""
        data = self.open_yaml()
        return data["HOST"]

    def get_department(self):
        data = self.open_yaml()
        return data["department"]



if __name__ == '__main__':
    read = ReadYaml("api.yaml")
    print(read.get_department())

