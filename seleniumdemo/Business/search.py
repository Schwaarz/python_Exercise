from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from seleniumdemo.Page_Object import baidupage,sunnypage,sinitekwhpage

driver = webdriver.Chrome()
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
    driver.find_element_by_xpath(sinitekwhpage.username).send_keys(username)
    driver.find_element_by_xpath(sinitekwhpage.password).send_keys(password)
    driver.find_element_by_xpath(sinitekwhpage.login_btn).click()
    time.sleep(3)
    text = driver.find_element_by_xpath(sinitekwhpage.tips).text
    return text


