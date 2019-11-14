from selenium import webdriver
import unittest
import case
from selenium.webdriver.support import expected_conditions
from pages.forest_animal_page import forestAnimalFun
import time

class forestAnimalTest(unittest.TestCase):
    """森林动植物-野生动物"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(case.test_http)
        cls.driver.implicitly_wait(10)
        cls.m = forestAnimalFun(cls.driver)
        cls.m.login()


    # 用例每次结束时执行
    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addAnimal_01(self):
        """新增档案-不输入任何数据"""
        # 进入到森林动植物-新增档案界面
        self.m.add_btn()
        self.m.input_xiaoban()
        time.sleep(5)
        self.m.submit_btn()
        # 确认按钮不可点击，则用例通过
        m = expected_conditions.element_to_be_clickable(('xpath', './/*/nz-modal/div/div[2]/div/div/div[3]/button[2]'))(self.driver)
        self.assertFalse(m)

    def test_addAnimal_02(self):
        """新增档案-仅输入必填项"""

        # 进入到森林动植物-新增档案界面
        self.m.add_data1("草兔", latitude='97.6262', longitude='38.2626')
        time.sleep(5)
        t = self.m.is_add_seccess('草兔')
        # 数据列表的名称中存在该名称，则用例通过
        self.assertTrue(t)

    def test_addAnimal_03(self):
        """新增档案-完整输入"""
        self.m.add_data1('角百灵', '98.2626', '37.2626', '15', '测试', 'D:\\测试\\测试视频\\荒漠猫.mp4')
        t = self.m.is_add_seccess('角百灵')

        # 数据列表的名称中存在该名称，则用例通过
        self.assertTrue(t)


if __name__ == '__main__':
    unittest.main()