import os
import re
from urllib.error import HTTPError
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve


def se_tu():
    while True:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get('https://api.vvhan.com/api/tao')
        data = driver.page_source  # 获取网页源代码
        soup = BeautifulSoup(data, 'html.parser')
        title = soup.find_all('title')
        result = re.findall('<title>(.*?)_', str(title))  # 获取标题
        img = soup.select('img')  # 提取img标签
        link = img[0]['src']  # 提取img的链接
        try:
            urlretrieve(link, 'd:/pic/' + str(result) + '.jpg')
            path = 'D:\ pic'
            mkdir = os.listdir(path)  # 获取已爬取目录图片数量
            print('成功！爬取第' + str(len(mkdir)) + '张图片')  # 爬取计数
        except HTTPError:
            print('触发异常，爬取失败')
            pass
        continue


se_tu()
