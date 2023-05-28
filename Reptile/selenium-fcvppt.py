from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def se_fcvppt():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # driver.set_window_position(0, -2000) 设置浏览器位置，使其跟无头一样的效果
    driver.get('https://spankbang.com/s/fc2ppv/?o=popular')
    time.sleep(1)
    driver.find_element("id", 'age_check_yes').click()
    time.sleep(10)
    driver.find_element('xpath', '/html/body/header/ul/li[3]/a[2]').click()
    time.sleep(120)
    driver.find_element('xpath', '//*[@id="log_username"]').send_keys('qq2071419073@gmail.com')
    time.sleep(1)
    driver.find_element('xpath', '//*[@id="log_password"]').send_keys('HekiFVC9zS,tZyB')
    time.sleep(1)
    driver.find_element('xpath', '//*[@id="auth_login_form"]/p[1]/button').click()
    time.sleep(3)
    driver.find_element('xpath', '/html/body/main/div[1]/div/div/div[1]/div[1]/a[1]/picture/img').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    driver.find_element('xpath', '//*[@id="video"]/div[1]/ul[1]/li[7]')
    data = driver.page_source  # 获取网页源代码
    # soup = BeautifulSoup(data, 'html.parser')
    # title = soup.find_all('title')
    print(data)


se_fcvppt()
