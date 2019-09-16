# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_picc.py
@time: 2019/9/16 20:55
@desc：picc 回归验收
"""
import unittest
from base.requests import Request
from base.headers import HEADER
from tools.log_tool import Logger
from tools.yaml_tool import ReadYaml



class TestPicc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host = ReadYaml("api.yaml").get_host()
        cls.request = Request()
        cls.log = Logger()
        cls.log.info("-------------------PICC STA-------------------")

    def setUp(self):
        self.log.info("----------CASE STA----------")

    def Ttest_department_add(self):
        case_name = "添加部门"
        url = self.host + "/web/department/add"
        param = {
            "name": "测试添加部门A",
            "notes": "部门名称不存在"
        }
        response = self.request.post_json(_url=url, _json=param, _headers=HEADER, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("操作成功", response.json()["message"])

    def test_departement_list(self):
        case_name = "部门列表显示"
        url = self.host + "/web/department/list"
        response = self.request.get(_url=url, _headers=HEADER, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("操作成功", response.json()["message"])

    def Ttest_serviceDivision_add(self):
        case_name = "添加测试分部"
        url = self.host + "/web/serviceDivision/add"
        param = {
            "departmentId": 22,
            "name": "测试服务分部A",
            "notes": "在ID为22的部门下，添加一个名叫测试服务分部A的服务分部",
            "serviceArea": [{
                "id": "510109",
                "value": "四川省成都市高新区"
            }]}
        response = self.request.post_json(_url=url, _json=param, _headers=HEADER, _case_name=case_name)
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("操作成功", response.json()["message"])

    def test_serviceDivision_list(self):
        case_name = "服务分部列表"
        url = self.host + "/web/serviceDivision/list"
        param = {
            "departmentId": 22,
            "name": "测试服务分部A"
        }
        response = self.request.get(_url=url, _data=param, _headers=HEADER, _case_name=case_name)
        print(response.json())
        self.log.info("【%s】 - 返回结果：%s" % (case_name, response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("操作成功", response.json()["message"])


    def tearDown(self):
        self.log.info("----------CASE END----------")

    @classmethod
    def tearDownClass(cls):
        cls.log.info("-------------------PICC END-------------------")


if __name__ == '__main__':
    unittest.main()
