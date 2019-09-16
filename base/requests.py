# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: requests.py
@time: 2019/9/16 14:18
@desc：封装requests请求
"""
import requests
from tools.log_tool import Logger


class Request:
    def __init__(self):
        self.log = Logger()
    def post_data(self, _url, _data, _headers, _case_name=None):
        """参数类型为:data"""
        self.log.info("【%s】 - 请求地址：%s" % (_case_name, _url))
        self.log.info("【%s】 - 请求参数: %s" % (_case_name, _data))
        response = requests.post(url=_url, data=_data, headers=_headers, _casename=None)
        self.log.info("【%s】 - 响应码: %d" % (_case_name, response.status_code))
        return response

    def post_json(self, _url, _json, _headers, _case_name=None):
        """参数类型为：json"""
        self.log.info("【%s】 - 请求地址：%s" % (_case_name, _url))
        self.log.info("【%s】 - 请求参数: %s" % (_case_name, _json))
        response = requests.post(url=_url, json=_json, headers=_headers)
        self.log.info("【%s】 - 响应码: %d" % (_case_name, response.status_code))
        return response

    def post_files(self, _url, _files, _headers, _case_name=None):
        """参数类型为：文件（上传文件）"""
        self.log.info("【%s】 - 请求地址：%s" % (_case_name, _url))
        self.log.info("【%s】 - 请求参数: %s" % (_case_name, _files))
        response = requests.post(url=_url, files=_files, headers=_headers)
        self.log.info("【%s】 - 响应码: %d" % (_case_name, response.status_code))
        return response

    def get(self, _url, _headers, _data=None, _case_name=None):
        """get请求，参数可为空"""
        self.log.info("【%s】 - 【请求地址：%s】" % (_case_name, _url))
        self.log.info("【%s】 - 【请求参数: %s】" % (_case_name, _data))
        response = requests.get(url=_url, params=_data, headers=_headers)
        self.log.info("【%s】 - 【响应码: %d】" % (_case_name, response.status_code))
        return response
