import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://www.jsons.cn/unicode/')
time.sleep(2)

# 获取所有菜单元素，存储到列表中
menu_items = driver.find_elements(By.CSS_SELECTOR, '.nav li')

for item in menu_items:
    # 获取菜单文本和链接地址
    menu_text = item.text
    menu_link = item.find_elements(By.TAG_NAME,'a')[0].get_attribute('href')

    # 输出菜单文本和链接地址
    print('菜单:', menu_text)
    print('链接:', menu_link)

    # 单击链接并验证页面是否加载成功
    link = item.find_elements(By.TAG_NAME,'a')[0]

    # 存储当前页面的URL
    current_url = driver.current_url

    driver.execute_script("arguments[0].click();", link)

    try:
        # 等待新页面加载完成
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        # 检查页面是否包含"404 - 找不到文件或目录"文本
        if '404 - 找不到文件或目录' in driver.page_source:
            print('链接无效！')
        else:
            # 获取新页面标题和URL
            new_title = driver.title
            new_url = driver.current_url
            print('新页面标题:', new_title)
            print('新页面URL:', new_url)
            print('链接有效！')

    except:
        pass

    # 返回上一页
    driver.execute_script("window.history.go(-1)")

    # 获取所有菜单元素，存储到列表中
    menu_items = driver.find_elements(By.CSS_SELECTOR, '.nav li')

driver.quit()
