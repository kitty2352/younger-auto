from selenium import webdriver
from common.base import Base
import time
# 登录类
class LoginYCW(Base):

    # 定位登录页面上的元素
    loc_user = ('xpath', '//*[@id="loginbox"]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input')
    loc_password = ('xpath', '//*[@id="loginbox"]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input')
    loc_lgbtn = ('class name', 'login-form-button')
    loc_lgalert = ('class name', 'ant-btn-primary')
    loc_autologin = ('xpath', '//*[@id="loginbox"]/form/nz-form-item[2]/nz-form-control/div/span/label/span[1]/input')
    loc_error_username = ('xpath', '//*[@id="loginbox"]/form/nz-form-item[1]/nz-form-control/div/nz-form-explain/div')
    loc_error_password = ('xpath', '//*[@id="loginbox"]/form/nz-form-item[2]/nz-form-control/div/nz-form-explain/div')

    def __init__(self, driver):
        self.driver = driver

    # 用户名输入框
    def input_user(self, text=''):
        self.send_keys(self.loc_user, text)

    # 密码输入框
    def input_psw(self, text=''):
        self.send_keys(self.loc_password, text)

    # 登录按钮
    def login_btn(self):
        self.click(self.loc_lgbtn)

    # 自动登录按钮
    def click_autologin(self):
        self.click(self.loc_autologin)

    def login(self, username, password):

        # 输入用户名
        self.send_keys(self.loc_user, username)
        # 输入密码
        self.send_keys(self.loc_password, password)
        # 点击确认按钮
        self.click(self.loc_lgbtn)
        self.click(self.loc_lgalert)

    # 获取错误结果
    def get_error_message_verify(self):
        msg = self.driver.find_element_by_id("error-box").text
        return msg

    # 用户名错误消息
    def get_error_message_username(self):
        return self.is_text_in_element(self.loc_error_username, "用户名")

    # 密码错误消息提示
    def get_error_message_password(self):
        return self.is_text_in_element(self.loc_error_password, "密码")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.121.31/login")
    ycw = LoginYCW(driver)
    # ycw.input_user("admin")
    # ycw.input_psw("123")
    # ycw.click_autologin()
    ycw.login_btn()
    print(ycw.get_error_message_username())
    print(ycw.get_error_message_password())
    time.sleep(2)
    driver.quit()