# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: path_tool.py
@time: 2019/9/16 14:36
@desc：获取文件路径
"""
import os


class FilePath:

    def root_path(self):
        """获取项目的根路径"""
        path = os.path.abspath(os.path.dirname(__file__)).split('auto_picc_api')[0]
        root = os.path.join(path, "auto_picc_api")
        return root

    def log_path(self):
        """日志文件"""
        root = self.root_path()
        return os.path.join(root, "logs")

    def conf_path(self):
        """配置文件"""
        root = self.root_path()
        return os.path.join(root, "conf")

    def excel_path(self):
        """测试数据"""
        root = self.root_path()
        return os.path.join(root, "data")
