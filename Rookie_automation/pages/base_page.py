from selenium.webdriver.support.wait import WebDriverWait

from config.read_config import ReadConf


class BasePage(object):
    """
    1、业务页面继承类
    2、对selenium底层方法进行二次封装
    """
    # 读取config.ini配置文件,传入sections值
    url = ReadConf()
    # 传入sections模块
    standard_url = url.readConf("ui_sections")
    # 这里传入sections模块中的url
    base_url = standard_url['url']

    def __init__(self, driver, test_url=base_url):
        """
        构造函数
        :param driver:
        :param test_url:
        """
        self.driver = driver
        self.url = test_url
        # 设置全局元素隐式等待时间为10秒
        self.driver.implicitly_wait(10)



    def open_url(self):
        """
        打开url
        :return:
        """
        url = self.url
        self.driver.get(url)
        # title = self.driver.title
        # print("项目名称： ", title)
        # # 获取当前页面的url
        # print("项目地址: ", self.driver.current_url)

    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :return:
        """
        self.driver.forward()

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()

    def find_element(self, *loc):
        """
        判断定位方式
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("元素在页面中未找到！", *loc)

    def find_elements(self, *loc):
        return self.driver.find_element(*loc)

    def input_content(self, loc, content):
        """
        文本框内容输入
        :param loc
        :param content
        """
        self.find_element(*loc).send_keys(content)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # getattr相当于self.loc
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.mouse_click(loc)  # 调用鼠标点击事件方法
            if clear_first:
                self.mouse_clear(loc)  # 调用鼠标清理事件方法
                self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def mouse_clear(self, loc):
        """
        鼠标清理事件
        :param loc
        """
        return self.find_element(*loc).clear()

    def mouse_click(self, loc):
        """
        鼠标点击事件
        :param loc
        """
        return self.find_element(*loc).click()

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    def isElementPresent(self, element_xpath):
        """
        封装一个函数，用来判断页面某个值是否存在
        :param element_xpath
        """
        try:
            self.driver.find_element_by_xpath(element_xpath)
            return True
        except:
            return False

