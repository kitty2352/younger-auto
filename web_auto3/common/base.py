from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class Base():

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 30
        self.t = 0.5

    """封装操作元素事件"""
    def findElementNew(self, locator):
        # 定位到元素，返回元素对象，没定位到就抛出异常
        ele = WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.presence_of_element_located(locator))
        # 参数使用错误判断
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
        return ele

    def findElements(self, loctor):
        elements = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_elements(*loctor))
        # 参数使用错误判断
        if not isinstance(loctor, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
        return elements

    def findElement(self, loctor):
        element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element(*loctor))
        # 参数使用错误判断
        if not isinstance(loctor, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
        return element

    def click(self, loctor):
        self.findElementNew(loctor).click()

    def send_keys(self, loctor, _text):
        self.findElementNew(loctor).send_keys(_text)

    def isElementExit(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExit2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到的元素个数：%s"%n)
            return True

    """封装判断"""
    def is_title(self, _title):
        # 判断浏览器的标题是否一致，返回布尔值
        result = WebDriverWait(self.driver, self.timeout, self.t).until(expected_conditions.title_is(_title))
        return result

    def is_title_contains(self, _title):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(expected_conditions.title_contains(_title))
        return result

    def is_text_in_element(self, locator, _text):
        result = WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.text_to_be_present_in_element(locator, _text))
        return result

    """封装鼠标悬停事件"""
    def move_to_element(self, locator):
        el = self.findElementNew(locator)
        ActionChains(driver).move_to_element(el).perform()

    """封装select方法"""
    def select_by_index(self, locator, index=0):
        element = self.findElementNew(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        element = self.findElementNew(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        element = self.findElementNew(locator)
        Select(element).select_by_visible_text(text)

    """js操作浏览器滚动条"""
    def js_scroll_end(self):
        # 滚动到页面底部
        js_height = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_height)

    def js_focus(self, locator):
        # 聚焦元素
        target = self.findElementNew(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
         # 回到顶部
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.hao123.com")
    bas = Base(driver)
    loc = ('xpath', '//*[@id="ad_title_id"]')
    bas.js_focus(loc)
    time.sleep(2)
    driver.quit()

