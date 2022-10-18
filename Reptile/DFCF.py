import io
import os
import re
import time

import requests
from PyPDF2 import PdfFileMerger
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://data.eastmoney.com/report/orgpublish.jshtml?orgcode=80000007')
# 翻页获取网页源代码，获取5页
data_all = ''
for i in range(3):
    driver.find_element("xpath", '//*[@id="gotopageindex"]').clear()
    driver.find_element("xpath", '//*[@id="gotopageindex"]').send_keys(i + 1)
    driver.find_element("xpath", '//*[@id="orgpublish_table_pager"]/div[2]/form/input[2]').click()
    time.sleep(3)
    data = driver.page_source  # 获取网页源代码
    data_all += data
soup = BeautifulSoup(data_all, 'html.parser')
link3 = []
link = soup.find_all(href=re.compile("/report/zw_"))  # 正则过滤获取研报子页面网址
link2 = soup.find_all(href=re.compile("/report/info"))
link3.append(link + link2)


# print(len(link3[0]))

# 下载PDF文件
def download_pdf(save_path, pdf_name, pdf_url, pdf_date):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    proxies = {
        'http': 'HTTP://60.170.204.30:8060'
    }
    response = requests.get(pdf_url, headers=send_headers, proxies=proxies)
    bytes_io = io.BytesIO(response.content)
    with open(save_path + pdf_date + "%s.PDF" % pdf_name, mode='wb') as f:
        f.write(bytes_io.getvalue())
        print(pdf_date + '%s.PDF,下载成功！' % (pdf_name))


# 下载东方财富研报
def Guosen_download():
    for a in link3:
        for i in a:
            sort_url = re.findall('"(.*?)"', str(i))  # 提取短网址
            YB_title = re.findall(r'>(.*?)</a>', str(i))  # 提取研报标题
            title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "",
                           str(YB_title))  # 去除特殊字符，只保留汉字，字母，数字
            url = 'https://data.eastmoney.com'  # 网址头
            report_url = url + sort_url[0]  # 拼接循环输出完整链接
            driver.get(report_url)
            data2 = driver.page_source
            soup2 = BeautifulSoup(data2, 'html.parser')
            pdf = soup2.find_all(href=re.compile("https://pdf"))  # 过滤PDF下载链接
            pdf_url = pdf[0]['href']  # 提取PDF地址
            date = soup2.find_all('span', id='publish-date')  # 提取研报日期
            date2 = re.findall(r'>(.*?)</span>', str(date))  # 正则过滤
            pdf_date = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "",
                              str(date2))  # 正则过滤
            save_path = 'D:/DFCF/'
            download_pdf(save_path, title, pdf_url, pdf_date)  # 调用下载函数


# 拼接PDF成大PDF
def pdf_pj():
    target_path = 'D:/DFCF/'
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.PDF')]
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]
    file_merger = PdfFileMerger()
    for pdf in pdf_lst:
        file_merger.append(pdf)  # 合并pdf文件
    file_merger.write("C:/Users/yinguohao/Downloads/guosenYB.pdf")


Guosen_download()
