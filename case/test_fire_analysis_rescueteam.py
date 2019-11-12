from selenium import webdriver
from pages.forest_fireProofing_analysis_page import forest_fireProofing_analysis
from pages.login_page import LoginYCW
import unittest
import time

class rescueteamTest(unittest.TestCase):
    """
    森林防火-防火资源分析-扑救队伍功能
    """

    # 用例前置条件
    @classmethod
    def setUpClass(cls):
        # 进入森林防火- 防火资源分析界面
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.121.31/login")
        cls.r = forest_fireProofing_analysis(cls.driver)
        cls.r.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    def test_add01(self):
        """新增扑救队伍-不输入任何数据"""
        self.r.addRescueTeam1('', '')
        self.assertTrue(self.r.messesge_is_exist())

    def test_add02(self):
        """新增扑救队伍-仅输入必填项"""
        self.r.addRescueTeam1('test03', '大河边上', lantitude='105.26226', longitude='38.2626')
        keyword = self.r.get_resource_name()
        self.assertTrue(self.r.get_search_result(keyword))

    def test_add03(self):
        """新增扑救队伍-完整输入"""
        self.r.addRescueTeam1('test04','环球中心海洋乐园', '张大大', '13625548526', '拖鞋：4，救生圈：10，手机：10，电脑：100', '98.2626', '37.26226', '纯属娱乐')
        keyword = self.r.get_resource_name()
        self.assertTrue(self.r.get_search_result(keyword))

    def test_add04(self):
        """新增扑救队伍-经纬度格式校验1"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_lantitude, "181")
        self.r.send_keys(self.r.loc_longitude, '95')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add05(self):
        """新增扑救队伍-经纬度格式校验2"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_lantitude, "-181")
        self.r.send_keys(self.r.loc_longitude, '-91')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add06(self):
        """新增扑救队伍-经纬度格式校验3"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_lantitude, "我vvfd ")
        self.r.send_keys(self.r.loc_longitude, '@151515')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add06(self):
        """新增扑救队伍-经纬度格式校验4"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_lantitude, "105.2626")
        self.r.send_keys(self.r.loc_longitude, '37.26266')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertFalse(result1 and result2)

    def test_delete01(self):
        """批量删除-空删除"""

        # 不选择任何数据，点击删除按钮
        self.r.click(self.r.loc_muldelete)
        m = self.r.get_delete_message()
        self.assertEqual(m, '请选择要删除的数据!')

    def test_delete02(self):
        """单项删除"""
        self.r.search("test")
        self.r.multDelete(self.r.loc_delete_choose_first)
        m = self.r.get_delete_message()
        self.assertEqual(m, '删除成功!')


    def test_delete03(self):
        """全选删除"""
        self.r.search("test")
        self.r.multDelete(self.r.loc_delete_choose_all)
        m = self.r.get_delete_message()
        self.assertEqual(m, '删除成功!')


if __name__ == '__main__':
    unittest.main()