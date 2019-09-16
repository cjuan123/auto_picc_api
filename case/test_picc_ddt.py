# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_picc_ddt.py
@time: 2019/9/16 14:28
@desc：使用unittest+ddt 框架完成自动化测试
        使用ddt来执行excel表中的测试用例，并进行自动化
"""
import unittest
import json
from tools.log_tool import Logger
from base.requests import Request
from base.headers import HEADER
from tools.excel_tool import ReadExcel
from tools.yaml_tool import ReadYaml
import ddt

@ddt.ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host = ReadYaml("api.yaml").get_host()
        cls.log = Logger()
        cls.log.info("-------------------PICC STA-------------------")
        cls.request = Request()
        cls.headers = HEADER

    def setUp(self):
        self.log.info("---------Case   STA---------")

    @ddt.data(*ReadExcel("case_data.xlsx").row_value("/web/department/add"))
    @ddt.unpack
    def Ttest_department_add(self, moudle, api, request_method, case_name, data, except_result, case_desc):
        """添加部门"""
        url = self.host + api
        response = self.request.post_json(_url=url, _json=json.loads(data), _headers=self.headers, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(except_result, response.json()["message"])
        self.assertEqual(200, response.status_code)

    @ddt.data(*ReadExcel("case_data.xlsx").row_value("/web/department/list"))
    @ddt.unpack
    def Ttest_department_list(self, moudle, api, request_method, case_name, data, except_result, case_desc):
        """部门列表"""
        url = self.host + api
        response = self.request.get(_url=url, _headers=self.headers, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(except_result, response.json()["message"])
        self.assertEqual(200, response.status_code)\

    @ddt.data(*ReadExcel("case_data.xlsx").row_value("/web/department/update"))
    @ddt.unpack
    def Ttest_department_update(self, moudle, api, request_method, case_name, data, except_result, case_desc):
        """编辑部门信息"""
        url = self.host + api
        response = self.request.post_json(_url=url,_json=json.loads(data), _headers=self.headers, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        print(response.json())
        self.assertEqual(except_result, response.json()["message"])
        self.assertEqual(200, response.status_code)

    @ddt.data(*ReadExcel("case_data.xlsx").row_value("/web/serviceDivision/add"))
    @ddt.unpack
    def test_serviceDivision_add(self, moudle, api, request_method, case_name, data, except_result, case_desc):
        """部门列表"""
        url = self.host + api
        response = self.request.post_json(_url=url, _json=json.loads(data), _headers=self.headers, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        print(response.json())
        self.assertEqual(except_result, response.json()["message"])
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        self.log.info("---------Case   END---------")

    @classmethod
    def tearDownClass(cls):
        cls.log.info("-------------------PICC END-------------------")

if __name__ == '__main__':
    unittest.main()