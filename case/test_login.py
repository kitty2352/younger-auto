from selenium import webdriver
import unittest
from pages.login_page import LoginYCW


class loginTest(unittest.TestCase):
    """
    测试登录功能
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginObj = LoginYCW(cls.driver)
        cls.driver.implicitly_wait(10)

    # 用例每次执行时运行
    def setUp(self):
        self.driver.get("http://192.168.121.31/login")

    # 用例每次结束时执行
    def tearDown(self):
        # 清空cookie
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_01(self):
        """登录-用户名和密码都输入正确"""
        self.loginObj.login("admin", "123")
        self.assertTrue(self.driver.current_url == 'http://192.168.121.31/dashboard')

    def test_login_02(self):
        """登录-用户名正确，密码错误"""
        self.loginObj.login("admin", "123456")
        self.assertTrue(self.loginObj.get_error_message_verify() == '密码错误')

    def test_login_03(self):
        """登录-用户名错误 密码正确"""
        self.loginObj.login("hahaha", "123456")
        # 通过断言方法判断是否登录成功
        self.assertTrue(self.loginObj.get_error_message_verify() == '用户名不存在')

    def test_login_04(self):
        """登录-不输入用户名和密码"""
        self.loginObj.login_btn()
        self.assertTrue(self.loginObj.get_error_message_username() and self.loginObj.get_error_message_password())

    def test_login_05(self):
        """登录-不输入用户名"""
        self.loginObj.input_psw("123")
        self.loginObj.login_btn()
        self.assertTrue(self.loginObj.get_error_message_username())

    def test_login_06(self):
        """登录-不输入密码"""
        self.loginObj.input_user("admin")
        self.loginObj.login_btn()
        self.assertTrue(self.loginObj.get_error_message_password())


if __name__ == '__main__':
    unittest.main()