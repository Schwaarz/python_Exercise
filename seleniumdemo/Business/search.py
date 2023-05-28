from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from seleniumdemo.Page_Object import baidupage,sunnypage,sinitekwhpage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# 无界面浏览器运行
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# 浏览器驱动自动安装适应
driver = webdriver.Chrome(ChromeDriverManager().install())
# 注意更换环境
driver.get(baidupage.url)

def baidu_search(string):
    driver.find_element("id", baidupage.search).send_keys(string)
    driver.find_element("id", baidupage.search).send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element("xpath", baidupage.click).click()
    title = driver.title
    return title

def qqyx_login(username,password):
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    time.sleep(1)
    driver.switch_to.frame(driver.find_element("xpath", baidupage.iframe))
    driver.find_element("xpath", baidupage.username).send_keys(username)
    driver.find_element("xpath", baidupage.password).send_keys(password)
    driver.find_element("xpath", baidupage.login_btn).click()
    time.sleep(1)
    driver.find_element("xpath", baidupage.username).clear()
    driver.find_element("xpath", baidupage.password).clear()
    text = driver.find_element("xpath", baidupage.tips).text
    return text

def sunny_login(username,password):
    time.sleep(3)
    driver.find_element("xpath", sunnypage.username).send_keys(username)
    driver.find_element("xpath", sunnypage.password).send_keys(password)
    driver.find_element("xpath", sunnypage.login_btn).click()
    time.sleep(3)
    text = driver.find_element("xpath", sunnypage.tips).text
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

# 获取菜单
def sinitek_api_memu():
    sinitekwh_login('admin','111')
    time.sleep(5)
    driver.find_element("xpath", sinitekwhpage.memu_search).send_keys('菜单配置')
    time.sleep(3)
    driver.find_element("CSS", sinitekwhpage.memu_i).click()
    time.sleep(3)
    driver.find_element("xpath", sinitekwhpage.search_memu).send_keys('')
    driver.find_element('att', sinitekwhpage.select_memu).click()
    # 配置功能url
    driver.find_element('xpath', sinitekwhpage.add_api).click()
    driver.find_element('xpath', sinitekwhpage.gnmc).send_keys()
    driver.find_element('xpath', sinitekwhpage.lx).click()
    driver.find_element('xpath', sinitekwhpage.lx_gndm).click()
    driver.find_element('xpath', sinitekwhpage.lxmc).send_keys()
    driver.find_element('xpath', sinitekwhpage.memu_url).send_keys()
    driver.find_element('xpath', sinitekwhpage.save_api).click()



