import time

import pytest
import allure
from pages.sinitek_menu_serach import Sinitek_Menu_Serachpage
from pages.sinitek_login import SiniTek_LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestCase():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    @allure.title('菜单搜索')
    def test_01(self):
        """搜索指定菜单名称"""
        SiniTek_LoginPage(driver=self.driver).login_operation_isexample('admin', '111')
        result = Sinitek_Menu_Serachpage(driver=self.driver).menu_serach('报告撰写')
        assert result == '报告撰写'

    @allure.title('菜单搜索2')
    def test_02(self):
        """搜索指定菜单名称"""
        SiniTek_LoginPage(driver=self.driver).login_operation_isexample('admin', '111')
        result = Sinitek_Menu_Serachpage(driver=self.driver).menu_serach('我的估值附件')
        assert result == '我的估值附件'

    @allure.title('菜单搜索3')
    def test_03(self):
        """搜索指定菜单名称"""
        SiniTek_LoginPage(driver=self.driver).login_operation_isexample('admin', '111')
        result = Sinitek_Menu_Serachpage(driver=self.driver).menu_serach('流程查看')
        assert result == '流程查看'

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'sinitek_menu_serach_case.py'])