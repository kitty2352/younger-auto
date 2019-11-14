from selenium import webdriver
from pages.forest_fireProofing_analysis_page2 import forest_fireProofing_analysis_page2
import case
import unittest
import time

class waterResourceTest(unittest.TestCase):
    """
    森林防火-防火资源分析-水源地功能
    """

    # 用例前置条件
    @classmethod
    def setUpClass(cls):
        # 进入森林防火- 防火资源分析-水源地界面
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(case.test_http)
        cls.r = forest_fireProofing_analysis_page2(cls.driver)
        cls.r.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    def test_add01(self):
        """新增水源地-不输入任何数据"""
        self.r.addWaterResource1('', '', '')
        self.assertTrue(self.r.messesge_is_exist())

    def test_add02(self):
        """新增水源地-仅输入必填项"""
        self.r.addWaterResource1('test04', '大河边上', '水库', latitude='105.26226', longitude='38.2626')
        keyword = self.r.get_resource_name()
        self.assertTrue(self.r.get_search_result(keyword))
        time.sleep(5)

    def test_add03(self):
        """新增水源地-完整输入"""
        self.r.addWaterResource1('test05', '环球中心海洋乐园', '堤坝', '人工', '888', '98.2626', '37.26226', '测试数据，仅供展示')
        keyword = self.r.get_resource_name()
        self.assertTrue(self.r.get_search_result(keyword))

    def test_add04(self):
        """新增水源地-经纬度格式校验1"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_latitude, "181")
        self.r.send_keys(self.r.loc_longitude, '95')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add05(self):
        """新增水源地-经纬度格式校验2"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_latitude, "-181")
        self.r.send_keys(self.r.loc_longitude, '-91')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add06(self):
        """新增水源地-经纬度格式校验3"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_latitude, "我vvfd ")
        self.r.send_keys(self.r.loc_longitude, '@151515')
        result1 = self.r.isElementExit(self.r.loc_errorLan_message)
        result2 = self.r.isElementExit(self.r.loc_errorLon_message)
        self.assertTrue(result1 and result2)

    def test_add06(self):
        """新增水源地-经纬度格式校验4"""
        self.r.click(self.r.loc_addButton)
        self.r.send_keys(self.r.loc_latitude, "105.2626")
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

    def test_pagination01(self):
        """分页-点击上一页(非首页)"""
        self.r.skip_page_to("3")
        pageNumber = self.r.get_current_page()
        if pageNumber == 1:
            return 1
        self.r.click_last_page()
        pageNumber = pageNumber-1
        self.r.click_last_page()
        pageNumber = pageNumber-1
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_pagination02(self):
        """分页-点击下一页(非最后一页)"""
        self.r.skip_page_to("3")
        pageNumber = self.r.get_current_page()
        if pageNumber == 1:
            return 1
        self.r.click_next_page()
        pageNumber = pageNumber + 1
        self.r.click_next_page()
        pageNumber = pageNumber + 1
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_pagination03(self):
        """分页-点击向后5页"""
        pageNumber = self.r.get_current_page()
        self.r.click_backward_five_to()
        if self.r.get_current_page() == 1:
            return 1
        pageNumber = pageNumber + 5
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_pagination04(self):
        """分页-点击向前5页"""
        self.r.skip_page_to(self.r.get_total_page())
        pageNumber = self.r.get_current_page()
        if pageNumber == 1:
            return 1
        self.r.click_forward_five_page()
        pageNumber = pageNumber - 5
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_pagination05(self):
        """分页-点击下一页(最后一页)"""
        pageNumber = self.r.get_current_page()
        self.r.click_last_page()
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_pagination06(self):
        """分页-点击上一页(非首页)"""
        self.r.skip_page_to(self.r.get_total_page())
        pageNumber = self.r.get_current_page()
        self.assertEqual(self.r.get_current_page(), pageNumber)

    def test_search01(self):
        """搜索-空搜索"""
        totalPage = self.r.get_total_page()
        self.r.search("")
        pageNumber = self.r.get_total_page()
        self.assertEqual(totalPage, pageNumber)

    def test_search02(self):
        """搜索-查询内容中包含字符"""
        result = self.r.get_search_result(".3. 2g")
        self.assertFalse(result)

    def test_search03(self):
        """搜索-模糊查询"""
        result = self.r.get_search_result("哈")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()