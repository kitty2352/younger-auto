from common.base import Base
from pages.login_page import LoginYCW
import time
from selenium import webdriver
class forest_fireProofing_analysis_page1(Base):

    resource_name = ''

    # 定位页面元素
    loc_fire = ('xpath', ".//*[text()='森林防火专题']")  # 首页防火专题按钮定位
    loc_fireProfing = ('xpath', './/*/nz-sider/div[1]/ul/li[7]/ul/ul/li[2]')  # 菜单栏中防火资源分析按钮
    loc_alert = ('xpath', '//*/nz-modal/div/div[2]/div/div/button')  # 指挥决策弹出关闭按钮
    loc_muldelete = ('xpath', './/app-analysis/div[2]/app-team/div[1]/div[2]/div[1]/button[1]')
    loc_position = ('xpath', './/app-analysis/div[2]/app-team/div[1]/div[2]/div[1]/button[2]')
    loc_addButton = ('xpath', './/app-analysis/div[2]/app-team/div[1]/div[2]/div[1]/button[3]')
    loc_inputlan = ('xpath', '//*[@id="cdk-overlay-6"]/nz-modal/div/div[2]/div/div/div/div/div[3]/input')
    loc_confirm = ('xpath', '//*[@id="cdk-overlay-6"]/nz-modal/div/div[2]/div/div/div/div/div[4]/button')

    # 新增输入框元素
    loc_resource_name = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[1]/nz-form-control/div/span/input')
    loc_location = ('xpath', '//*//nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[2]/nz-form-control/div/span/input')
    loc_department = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[3]/nz-form-control/div/span/app-cascader-xb/nz-cascader/div/div/span')
    loc_department_glj = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[1]/li')
    loc_department_bhz_1 = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[2]/li[1]')
    loc_department_bhz_2 = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[2]/li[2]')
    loc_department_bhz_3 = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[2]/li[3]')
    loc_department_bhz_4 = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[2]/li[4]')
    loc_department_bhz_5 = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[2]/li[5]')
    loc_department_xb = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[3]/li[1]')
    loc_department_lb = ('xpath', '//*[@class="cdk-overlay-pane"]/div/ul[4]/li[1]')
    loc_responsible = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[4]/nz-form-control/div/span/input')
    loc_phone_number = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[5]/nz-form-control/div/span/input')
    loc_phone_device = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[6]/nz-form-control/div/span/input')
    loc_latitude = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[7]/nz-form-control/div/span/input')
    loc_longitude = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[8]/nz-form-control/div/span/input')
    loc_remark = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[9]/nz-form-control/div/span/textarea')
    loc_savebtn = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/div/button')
    loc_errorLan_message = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[7]/nz-form-control/div/nz-form-explain/div')
    loc_errorLon_message = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/form/nz-form-item[8]/nz-form-control/div/nz-form-explain/div')

    # 搜索功能元素定位
    loc_search_input = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[2]/div[2]/input')
    loc_search_btn = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[2]/div[2]/button')
    loc_search_datas = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[3]/nz-table/nz-spin/div/div/div/div/div[2]/table/tbody/tr')

    # 删除功能元素定位
    loc_delete_message = ('xpath', '//*[@class="cdk-overlay-pane"]/nz-message-container/div/nz-message')
    loc_delete_choose_first = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[3]/nz-table/nz-spin/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/label/span[1]/input')
    loc_delete_choose_all = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[3]/nz-table/nz-spin/div/div/div/div/div[1]/table/thead/tr/th[1]/span/div/span/label/span[1]/input')
    loc_delete_confirm = ('xpath', '//*/nz-modal/div/div[2]/div/div/div/div/div[2]/button[2]')
    loc_delete_cancel = ('xpath', '//*/nz-modal/div/div[2]/div/div/div/div/div[2]/button[1]')

    # 分页功能元素
    loc_pagination1 = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[4]/nz-pagination/ul')
    loc_pagination = ('css selector', 'app-analysis>div.dummy>app-team>div.left>div.pagination>nz-pagination>ul>li:nth-last-child(2)')
    loc_lastPage = ('xpath', '//*/app-analysis/div[2]/app-team/div[1]/div[4]/nz-pagination/ul/li[1]/button')
    loc_nextPage = ('css selector', 'app-analysis>div.dummy>app-team>div.left>div.pagination>nz-pagination>ul>li:last-child>button')
    loc_allPage = ('css selector', 'app-analysis>div.dummy>app-team>div.left>div.pagination>nz-pagination>ul>li')

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        lg = LoginYCW(self.driver)
        lg.login("admin", "123")
        # 点击森林防火按钮
        time.sleep(2)
        self.click(self.loc_fire)
        # 关闭弹出
        time.sleep(2)
        self.findElements(self.loc_alert)[0].click()
        # 点击防火资源分析
        time.sleep(2)
        self.click(self.loc_fireProfing)

    """新增模块"""
    # 输入队伍名称
    def input_resource_name(self, resource_name):
        self.send_keys(self.loc_resource_name, resource_name)

    # 获取队伍名称
    def get_resource_name(self):
        return self.resource_name

    # 输入队伍地点
    def input_loc_location(self, loc_location):
        self.send_keys(self.loc_location, loc_location)

    # 选择所属管理
    def chooseDepartment(self):
        self.click(self.loc_department)
        self.click(self.loc_department_glj)
        self.click(self.loc_department_bhz_1)
        self.click(self.loc_department_xb)
        self.click(self.loc_department_lb)

    # 输入联系人
    def input_loc_responsible(self, loc_responsible):
        self.send_keys(self.loc_responsible, loc_responsible)

    # 输入联系电话
    def input_loc_phone_number(self, loc_phone_number):
        self.send_keys(self.loc_phone_number, loc_phone_number)

    # 输入设备
    def input_loc_phone_device(self, loc_phone_device):
        self.send_keys(self.loc_phone_device, loc_phone_device)

    # 输入经度
    def input_loc_latitude(self, loc_latitude):
        self.send_keys(self.loc_latitude, loc_latitude)

    # 输入纬度
    def input_loc_longitude(self, loc_longitude):
        self.send_keys(self.loc_longitude, loc_longitude)

    # 输入备注
    def input_remark(self, loc_remark):
        self.send_keys(self.loc_remark, loc_remark)

    def messesge_is_exist(self):
        return self.isElementExit(self.loc_errorLan_message)

    # 添加方法(不带参)
    def addRescueTeam(self):
        self.click(self.loc_addButton)

        self.input_resource_name("测试01")
        self.input_loc_location('大河坝边上')
        self.chooseDepartment()
        self.input_loc_responsible('哇哈哈')
        self.input_loc_phone_number("15232523625")
        self.input_loc_phone_device('火把：10，电话：20')
        self.input_loc_latitude('105.2626')
        self.input_loc_longitude('37.2626')
        self.input_remark("测试233333333")
        self.click(self.loc_savebtn)
        time.sleep(5)

    # 添加方法（带参）
    def addRescueTeam1(self, resource_name, location, responsible='', phone_number='', phone_device='', latitude='', longitude='', remark=''):
        # 获取队伍名称
        self.resource_name = resource_name
        # 点击添加按钮
        self.click(self.loc_addButton)
        # 输入。。。
        self.input_resource_name(resource_name)
        self.input_loc_location(location)
        self.chooseDepartment()
        self.input_loc_responsible(responsible)
        self.input_loc_phone_number(phone_number)
        self.input_loc_phone_device(phone_device)
        self.input_loc_latitude(latitude)
        self.input_loc_longitude(longitude)
        self.input_remark(remark)

        # 点击保存按钮
        self.click(self.loc_savebtn)
        time.sleep(5)

    """搜索模块"""
    # 搜索
    def search(self, keyword):
        self.send_keys(self.loc_search_input, keyword)
        self.click(self.loc_search_btn)

    # 获取搜索结果
    def get_search_result(self, keyword):
        self.search(keyword)
        if bool(1-self.isElementExit(self.loc_search_datas)):
            print("查询结果为空")
            return False
        else:
            for i in self.findElements(self.loc_search_datas):
                print("搜索中")
                if keyword in i.text:
                    return True
                    break
                else:
                    print("未匹配")
                    return False
                    break

    """删除模块"""
    # 删除功能
    def multDelete(self, element):
        # 选中元素
        self.click(element)
        # 点击批量删除
        self.click(self.loc_muldelete)
        # 点击确认按钮
        self.click(self.loc_delete_confirm)

    # 删除提示消息
    def get_delete_message(self):
        return self.findElement(self.loc_delete_message).text

    """分页模块"""
    # 获取当前总页数
    def get_total_page(self):
        return self.findElement(self.loc_pagination).get_attribute("title")

    # 获取当前页
    def get_current_page(self):
        return int(self.findElement(self.loc_pagination1).find_element_by_class_name('ant-pagination-item-active').text)

    # 判断页数是否存在
    def page_is_exit(self, pageNumber):
        flag = False
        for i in self.findElements(self.loc_allPage):
            if i.text == pageNumber:
                flag = True
                break
            else:
                flag = False
        return flag

    # 跳转到某页
    def skip_page_to(self, pageNumber):
        if int(pageNumber) > int(self.get_total_page()):
            print("页数输入不正确")
        else:
            if self.page_is_exit(pageNumber):
                self.findElement(self.loc_pagination1).find_element_by_link_text(pageNumber).click()
            else:
                self.click_backward_to()
                self.skip_page_to(pageNumber)

    # 点击下一页
    def click_last_page(self):
        self.click(self.loc_lastPage)

    # 点击上一页
    def click_next_page(self):
        self.click(self.loc_nextPage)

    # 点击向前5页
    def click_forward_five_page(self):
        for i in self.findElements(self.loc_allPage):
            if i.get_attribute("title") == '向前 5 页':
                i.click()
                break

    # 点击向后5页
    def click_backward_five_to(self):
        for i in self.findElements(self.loc_allPage):
            if i.get_attribute("title") == '向后 5 页':
                i.click()
                break