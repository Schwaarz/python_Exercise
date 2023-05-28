import time

import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.sinitek_login import SiniTek_LoginPage


class TestCase():
    @classmethod
    def setup_class(cls):
        print("执行前操作")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    @allure.title("输入为空")
    def test_01(self):
        result = SiniTek_LoginPage(driver=self.driver).login_operation_counterexample(' ', ' ')
        assert result == '请输入用户名和密码'

    @allure.title("只输入密码")
    def test_02(self):
        result = SiniTek_LoginPage(driver=self.driver).login_operation_counterexample('', '111')
        assert result == '请输入用户名和密码'

    @allure.title("只输入账号")
    def test_03(self):
        result = SiniTek_LoginPage(driver=self.driver).login_operation_counterexample('admin', '')
        assert result == '请输入用户名和密码'

    @allure.title("输入正确密码账号")
    def test_04(self):
        result = SiniTek_LoginPage(driver=self.driver).login_operation_isexample('admin', '111')
        assert result == '个人中心'
        if result == '个人中心':
            print('登录成功')


    @classmethod
    def teardown_class(cls):
        print("执行后操作")
        time.sleep(1)
        cls.driver.quit()

    # def setup_method(self):
    #     print("setup_method:  每个用例开始前执行")
    #
    # def teardown_method(self):
    #     print("teardown_method:  每个用例结束后执行")


if __name__ == '__main__':
    pytest.main(['-s', 'sinitek_login_pytest.py'])
