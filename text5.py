#面向对象
from seleniumdemo import webdriver
from time import  sleep
#Test这个类，
class Test():
    def __init__(self):
        self.dr=webdriver.Chrome()

    #打开网页
    def getUrl(self,url):
        return  self.dr.get(url)

     #输入文本
    def input_text(self,locator,text):
        return self.by_id(locator).send_keys(text)

    #点击搜索
    def click_btn(self,locator):
        return self.by_css(locator).click()

    #关闭浏览器
    def close_brower(self):
        self.dr.quit()

    #断言
    def assert_text(self):
        try:
            sleep(3)
            if 'demo' in self.dr.title:
                print('断言成功')
        except Exception as message:
            print('断言失败')

   #将各个步骤整合到一个函数，再次封装
    def all_actions(self,url,loc1,text,loc2):
        self.getUrl(url)
        self.input_text(loc1,text)
        self.click_btn(loc2)
        sleep(3)
        self.assert_text()
        self.close_brower()


#将id,name等封装起来，方便使用
    #id定位
    def by_id(self,locator):
        return self.dr.find_element_by_id(locator)

    # name定位
    def by_name(self,locator):
        return self.dr.find_element_by_name(locator)

    #link_text定位
    def by_link_text(self,locator):
        return self.dr.find_element_by_link_text(locator)

    #css定位
    def by_css(self,locator):
        return self.dr.find_element_by_css_selector(locator)

    # xpath定位
    def by_xpath(self,locator):
        return self.dr.find_element_by_xpath(locator)



#面向对象，按步骤执行
# L=Test()
# L.getUrl('http://www.baidu.com')
# L.input_text('kw','demo')
# L.click_btn('#su')
# sleep(2)
# L.close_brower()


#面向对象，一步到位
L=Test()
L.all_actions('http://www.baidu.com','kw','demo','#su')