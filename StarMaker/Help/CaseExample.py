#coding=utf-8
import time
import unittest
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver


#定义一个XXX测试类
class XXX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        pass

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_XXX(self):
        pass


if __name__ == "__main__":
    pass