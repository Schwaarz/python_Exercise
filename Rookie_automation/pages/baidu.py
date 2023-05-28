from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BaiduPage(BasePage):
    # 通过id方式定位元素
    search_loc = (By.ID, "kw")
    btn_loc = (By.ID, "su")

    # 操作步骤拆分封装
    def input_search(self, search):
        self.find_element(*self.search_loc).send_keys(search)

    def clk_search(self):
        self.find_element(*self.btn_loc).click()

    # 操作整合
    def baidu_search(self, search):
        self.open_url()
        self.input_search(search)
        self.clk_search()

