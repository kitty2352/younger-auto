from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions
from pages.forest_animal_page import forestAnimalFun


class forestAnimalTest(unittest.TestCase):
    """森林动植物-野生动物"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.121.31")
        cls.driver.implicitly_wait(10)
        cls.m = forestAnimalFun(cls.driver)
        cls.m.login()

    def setUp(self):
        # 进入到森林动植物-新增档案界面
        self.m.add_btn()

    # 用例每次结束时执行
    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addAnimal_01(self):
        """新增档案-不输入任何数据"""

        self.m.submit_btn()

        # 确认按钮不可点击，则用例通过
        m = expected_conditions.element_to_be_clickable(('xpath', './/*/nz-modal/div/div[2]/div/div/div[3]/button[2]'))(self.driver)
        self.assertFalse(m)

    def test_addAnimal_02(self):
        """新增档案-仅输入必填项"""

        self.m.input_name("藏原羚")
        self.m.input_longitude("104.325332")
        self.m.input_lantitude("37.665545")
        self.m.submit_btn()

        t = self.m.is_add_seccess('藏原羚')

        # 数据列表的名称中存在该名称，则用例通过
        self.assertTrue(t)