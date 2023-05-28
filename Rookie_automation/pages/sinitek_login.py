from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SiniTek_LoginPage(BasePage):

    # 定位器
    username = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div/input')
    password = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[3]/div/div/input')
    login_btn = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[4]/div/button')
    tips = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/p[2]')
    user_Home = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/a')

    # 步骤封装
    def send_username(self, username):
        self.find_element(*self.username).send_keys(username)

    def send_password(self, password):
        self.find_element(*self.password).send_keys(password)

    def login_btn_click(self):
        self.find_element(*self.login_btn).click()

    def tips_text(self):
        return self.find_element(*self.tips).text

    def login_success(self):
        return self.find_element(*self.user_Home).text

    #操作
    def login_operation_counterexample(self, username, password):
        self.open_url()
        self.send_username(username)
        self.send_password(password)
        self.login_btn_click()
        failure_text = self.tips_text()
        return failure_text

    def login_operation_isexample(self, username, password):
        self.open_url()
        self.send_username(username)
        self.send_password(password)
        self.login_btn_click()
        success_text = self.login_success()
        return success_text


