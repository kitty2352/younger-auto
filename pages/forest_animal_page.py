from selenium import webdriver
import time
from pages.login_page import LoginYCW
from common.base import Base
# from pykeyboard import PyKeyboard

class forestAnimalFun(Base):

    # 定位页面上的元素
    loc_animal = ('xpath', './/*/app-dashboard/div/footer/div[6]/div[1]/img')  # 首页中的森林动植物专题
    loc_wild_animal = ('xpath', './/*/nz-sider/div[1]/ul/li[9]/ul/ul/li[1]/span/span')  # 侧边栏中的森林动植物下的野生动物
    loc_addbtn = ('xpath', './/*/app-detail-home/nz-layout/nz-layout/nz-content/app-animal/nz-layout/div/div/button[2]')  # 新增档案按钮
    loc_submit = ('xpath', './/*/nz-modal/div/div[2]/div/div/div[3]/button[2]')  # 新增档案中的确认按钮

    # 新增档案中的元素
    loc_xiaoban = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/div/input')
    loc_name = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/div/input')
    loc_longitude = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[4]/nz-form-control/div/span/input')
    loc_latitude = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[5]/nz-form-control/div/span/input')
    loc_number = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[6]/nz-form-control/div/span/input')
    loc_record_person = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[7]/nz-form-control/div/span/input')
    loc_upload_movie = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[9]/nz-form-control/div/span/input')
    loc_upload_picture = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/div/div/div/input')
    loc_department = ('xpath', '//*/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/div/input')

    def __init__(self, driver):
        self.driver = driver

    # 上传图片
    # def upload_img(self):
    #     k = PyKeyboard()
    #     self.click(self.loc_upload_picture)
    #     time.sleep(2)
    #     # k.tap_key(k.shift_key)  # 切换成英文
    #     k.type_string('D:\\pic\\a.jpg')  # 打开文件所在目录
    #     time.sleep(2)
    #     k.tap_key(k.enter_key)
    #     time.sleep(1)
    #     k.tap_key(k.enter_key)

    # 新增档案中输入名称
    def input_name(self,text):
        self.send_keys(self.loc_name, text)

    # 新增档案中设置小班
    def input_xiaoban(self):
        self.send_keys(self.loc_department, '甘肃盐池湾国家级自然保护区管理局')

    # 新增档案中输入经度
    def input_longitude(self, text):
        self.send_keys(self.loc_longitude, text)

    # 新增档案中输入纬度
    def input_lantitude(self, text):
        self.send_keys(self.loc_latitude, text)

    # 新增档案中输入数量
    def input_number(self, text):
        self.send_keys(self.loc_number, text)

    # 新增档案中输入录入人
    def input_record_person(self, text):
        self.send_keys(self.loc_record_person, text)

    # 上传视频
    def upload_movie(self, url):
        self.send_keys(self.loc_upload_movie, url)
        time.sleep(5)

    # 新增档案
    def add_btn(self):
        self.click(self.loc_addbtn)

    # 提交表单
    def submit_btn(self):
        self.click(self.loc_submit)

    def login(self):
        lg = LoginYCW(self.driver)
        lg.login("admin", "123")
        # 点击森林动植物按钮
        self.click(self.loc_animal)
        # 点击野生动物
        self.click(self.loc_wild_animal)

    # 进入到森林动植物界面-新增档案界面
    def add_data(self):
        # 点击新增档案按钮
        self.add_btn()
        self.input_name("灰鹤")
        self.input_xiaoban()
        # 输入数据
        self.input_longitude('105.235')
        self.input_lantitude('37.25152')
        self.input_number(20)
        self.input_record_person('测试人员')
        self.upload_movie('D:\\测试\\测试视频\\01.mp4')
        # 点击确认按钮
        self.submit_btn()

    def add_data1(self, name, latitude, longitude, number='1', recordPerson= '', moviesUrl= 'D:\\测试\\测试视频\\01.mp4'):
        # 点击新增档案按钮
        self.add_btn()
        # self.upload_img()
        self.input_name(name)
        self.input_xiaoban()
        # 输入数据
        self.input_longitude(latitude)
        self.input_lantitude(longitude)
        self.input_number(number)
        self.input_record_person(recordPerson)
        self.upload_movie(moviesUrl)
        # 点击确认按钮
        self.submit_btn()


    def is_add_seccess(self, _text):
        res = self.is_text_in_element(('xpath', './/*/app-animal/nz-layout/div/nz-content/app-table-public/div/nz-table/nz-spin/div/div/div/div/div[2]/table/tbody'), _text)
        return res


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.121.31/login")
    m = forestAnimalFun(driver)
    m.login()
    m.add_data()
    t = m.is_add_seccess("灰鹤")
    print(t)
    driver.quit()


