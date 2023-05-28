import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.sinitek_login import SiniTek_LoginPage

class TestChromeDriverManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    # 输入为空
    def test02(self):
        self.assertEqual(SiniTek_LoginPage(driver=self.driver).login_operation_counterexample('', ''), '请输入用户名和密码')

    # 只输入密码
    def test03(self):
        self.assertEqual(SiniTek_LoginPage(driver=self.driver).login_operation_counterexample('', '111'), '请输入用户名和密码')

    # 只输入用户名
    def test04(self):
        self.assertEqual(SiniTek_LoginPage(driver=self.driver).login_operation_counterexample('admin', ''), '请输入用户名和密码')

    # 正常输入
    def test01(self):
        self.assertEqual(SiniTek_LoginPage(driver=self.driver).login_operation_isexample('admin', '111'), '个人中心')


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()