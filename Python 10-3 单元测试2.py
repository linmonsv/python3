#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import unittest

from test10_3_mydict import Dict

class TestDict(unittest.TestCase):
    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行。
    def setUp(self):
        print("setUp...")
    def tearDown(self):
        print("tearDown...")

    # 以test开头的方法就是测试方法，
    # 不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a = 1, b = "test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")
    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行单元测试
# 最简单的运行方式是在mydict_test.py的最后加上两行代码：
# 这样就可以把mydict_test.py当做正常的python脚本运行
if __name__ == "__main__":
    unittest.main()

# 另一种方法是在命令行通过参数-m unittest直接运行单元测试
# python3 -m unittest mydict_test

# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
