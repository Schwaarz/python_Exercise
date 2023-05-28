import os
import re
import threading
import time
from urllib.error import HTTPError
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


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
            path = 'D:/pic'
            mkdir = os.listdir(path)  # 获取已爬取目录图片数量
            print('成功！爬取第' + str(len(mkdir)) + '张图片')  # 爬取计数
        except HTTPError:
            print('触发异常，爬取失败')
            pass
        continue

# 多线程下载
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            se_tu()
            time.sleep(1)
            print(self.name, i)


t1 = MyThread()
t2 = MyThread()
t3 = MyThread()
t1.start()
t2.start()
t3.start()
print(threading.enumerate())
