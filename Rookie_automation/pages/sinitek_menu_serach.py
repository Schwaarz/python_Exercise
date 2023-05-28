from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Sinitek_Menu_Serachpage(BasePage):

    # 定位器
    icon_serach = (By.XPATH, '//*[@id="app"]/div/div[1]/header/div[2]/div[1]/div/span/i')
    menu_input = (By.XPATH, '//*[@id="app"]/div/div[1]/header/div[2]/div[1]/div[1]/input')
    Current_page = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/a[2]')

    # 步骤封装
    def input_menu(self, menu_value):
        self.find_element(*self.menu_input).send_keys(menu_value)

    def serach_click(self):
        self.find_element(*self.icon_serach).click()

    def Current_page_name(self):
        return self.find_element(*self.Current_page).text

    # 操作
    def menu_serach(self, menu_value):
        self.input_menu(menu_value)
        self.serach_click()
        current_page_name = self.Current_page_name()
        return current_page_name

