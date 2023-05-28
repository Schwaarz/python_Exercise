from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Add_Customer_Page(BasePage):

    # 名片
    business_card = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[1]/div[2]/div/div[1]/div/div/div/div/input')
    # 公司名称
    Company_name = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[2]/div/div/div/div/input')
    # 注册地址下拉框
    Registered_address_drop_down = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[6]/div/div[1]/div/span/span')
    zhuce_sheng = (By.XPATH, '/html/body/div[2]/ul[1]/li[1]')
    zhuce_shi = (By.XPATH, '/html/body/div[2]/ul[2]/li[1]')
    zhuce_qu = (By.XPATH, '/html/body/div[2]/ul[3]/li[1]')
    zhuce_jiedao = (By.XPATH, '/html/body/div[2]/ul[4]/li[1]')
    Registered_address = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[6]/div/div[2]/div/div/input')
    # 机器放置地址
    Machine_placement_address_drop_down = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[9]/div/div[1]/div/span/span')
    jiqi_sheng = (By.XPATH, '/html/body/div[3]/ul[1]/li[1]')
    jiqi_shi = (By.XPATH, '/html/body/div[3]/ul[2]/li[1]')
    jiqi_qu = (By.XPATH, '/html/body/div[3]/ul[3]/li[1]')
    jiqi_jiedao = (By.XPATH, '/html/body/div[3]/ul[4]/li[1]')
    Machine_placement_address = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[9]/div/div[2]/div/div/input')
    # 办公电话
    Office_phone = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[10]/div/div[1]/div/div/input')
    # 传真号码
    Fax_number = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[11]/div/div[1]/div/div/input')
    # 联系人姓名
    Contact_name = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[12]/div/div/div[3]/table/tbody/tr/td[1]/div/div/input')
    # 联系电话
    Contact_number = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[12]/div/div/div[3]/table/tbody/tr/td[2]/div/div/input')
    # 职务
    Office_drop_down = (By.XPATH, '//*[@id="panelContent"]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/form/div/div[12]/div/div/div[3]/table/tbody/tr/td[3]/div/div/div[1]/input')
    Office = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')
    # 提交按钮
    submit_button = (By.XPATH, '')

    # 操作步骤封装
    def input_gsmc(self,gsmc):
        self.find_element(*self.Contact_name).send_keys(gsmc)

    def input_zcdz(self, zcdz):
        self.find_element(*self.Registered_address_drop_down).click()
        self.find_element(*self.zhuce_sheng).click()
        self.find_element(*self.zhuce_shi).click()
        self.find_element(*self.zhuce_qu).click()
        self.find_element(*self.zhuce_jiedao).click()
        self.find_element(*self.Registered_address).send_keys(zcdz)

    def input_jqdz(self, jqdz):
        self.find_element(*self.Machine_placement_address_drop_down).click()
        self.find_element(*self.jiqi_sheng).click()
        self.find_element(*self.jiqi_shi).click()
        self.find_element(*self.jiqi_qu).click()
        self.find_element(*self.jiqi_jiedao).click()
        self.find_element(*self.Machine_placement_address).send_keys(jqdz)

    def input_bgdh(self, bgdh):
        self.find_element(*self.Office_phone).send_keys(bgdh)

    def input_czhm(self, czhm):
        self.find_element(*self.Fax_number).send_keys(czhm)

    def input_lxrxm(self, lxrxm):
        self.find_element(*self.Contact_name).send_keys(lxrxm)

    def input_lxdh(self, lxdh):
        self.find_element(*self.Contact_number).send_keys(lxdh)

    def input_zw(self):
        self.find_element(*self.Office_drop_down).click()
        self.find_element(*self.Office).click()

    def input_mp(self):
        self.find_element(*self.business_card)

    # 步骤整合
    def linshibaohu(self,gsmc,zcdz,jqdz):
        self.input_gsmc(gsmc)
        self.input_zcdz(zcdz)
        self.input_jqdz(jqdz)


