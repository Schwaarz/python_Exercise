from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from seleniumdemo.Page_Object import baidupage,sunnypage,sinitekwhpage
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(sinitekwhpage.url)

def baidu_search(string):
    driver.find_element_by_id(baidupage.search).send_keys(string)
    driver.find_element_by_id(baidupage.search).send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_xpath(baidupage.click).click()
    title = driver.title
    return title

def qqyx_login(username,password):
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    time.sleep(1)
    driver.switch_to.frame(driver.find_element_by_xpath(baidupage.iframe))
    driver.find_element_by_xpath(baidupage.username).send_keys(username)
    driver.find_element_by_xpath(baidupage.password).send_keys(password)
    driver.find_element_by_xpath(baidupage.login_btn).click()
    time.sleep(1)
    driver.find_element_by_xpath(baidupage.username).clear()
    driver.find_element_by_xpath(baidupage.password).clear()
    text = driver.find_element_by_xpath(baidupage.tips).text
    return text

def sunny_login(username,password):
    time.sleep(3)
    driver.find_element_by_xpath(sunnypage.username).send_keys(username)
    driver.find_element_by_xpath(sunnypage.password).send_keys(password)
    driver.find_element_by_xpath(sunnypage.login_btn).click()
    time.sleep(3)
    text = driver.find_element_by_xpath(sunnypage.tips).text
    return text

def sinitekwh_login(username,password):
    time.sleep(3)
    driver.find_element("xpath", sinitekwhpage.username).send_keys(username)
    driver.find_element("xpath", sinitekwhpage.password).send_keys(password)
    driver.find_element("xpath", sinitekwhpage.login_btn).click()
    time.sleep(1)
    driver.find_element("xpath", sinitekwhpage.username).clear()
    driver.find_element("xpath", sinitekwhpage.password).clear()
    text = driver.find_element("xpath", sinitekwhpage.tips).text
    return text
# 获取菜单值
def sinitekwh_memu():
    sinitekwh_login('admin','111')
    time.sleep(5)
    driver.maximize_window()
    # 循环获取菜单值并放入字典
    list = {}
    for i in range(1,8):
        list1 = driver.find_element("/html/body/div[1]/div/div[1]/header/div[1]/div["+str(i)+"]/div[1]/span").text
        list2 = "/html/body/div[1]/div/div[1]/header/div[1]/div["+str(i)+"]/div[1]/span"
        list.update({list1:list2})
    # 悬浮元素
    ActionChains(driver).move_to_element(driver.find_element(list['首页'])).perform()
    time.sleep(5)
    list2_1 = {}
    for a in range(1,10):
        list3 = driver.find_element("/html/body/div[1]/div/div[1]/header/div[1]/div[1]/div[2]/ul/li/ul/li["+str(a)+"]/a/div").text
        list4 = "/html/body/div[1]/div/div[1]/header/div[1]/div[1]/div[2]/ul/li/ul/li["+str(a)+"]/a/div"
        list2_1.update({list3:list4})
    return list,list2_1

# print(sinitekwh_memu())
