import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.baidu import BaiduPage

class Tsetbaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test01(self):
        BaiduPage(driver=self.driver).baidu_search("搜索")

    def test02(self):
        BaiduPage(driver=self.driver).baidu_search("软件测试")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()