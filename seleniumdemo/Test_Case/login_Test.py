import unittest
from seleniumdemo.Business import search
# 使用unittest进行断言
class BaiduTest(unittest.TestCase):
    def test01(self):
        self.assertEqual(search.baidu_search('QQ邮箱'), 'QQ邮箱_百度搜索')
    def test02(self):
        self.assertEqual(search.qqyx_login('', ''), '你还没有输入帐号！')
    def test03(self):
        self.assertEqual(search.qqyx_login('2071419073@qq.com',4),'你还没有输入验证码！')
    def test04(self):
        self.assertEqual(search.qqyx_login(1, 2), '请输入正确的帐号！')
class sunnyTest(unittest.TestCase):
    def test01(self):
        self.assertEqual(search.sunny_login('内审员','htsunny123'),'待审批客户')
if __name__ == '__main__':
    unittest.main()

