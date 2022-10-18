import requests
import urllib3
from bs4 import BeautifulSoup
import os
from PIL import Image
from io import BytesIO
import time
import random

urllib3.disable_warnings()
def api():
    url = 'https://a7a7.net/meitu/'
    re = requests.get(url,verify=False)
    soup = BeautifulSoup(re.content,'html.parser')
    itmes = soup.find_all('a')
    str2 = []
    str4 = {1: '#',
            2: 'https://a7a7.net/meitu/',
            3: 'https://a7a7.net/meitu/admin/register.php',
            4: 'https://a7a7.net/meitu/index.php/category/video/#cate_video',
            5: 'https://a7a7.net/meitu/admin/login.php?referer=https%3A%2F%2Fa7a7.net%2Fmeitu%2F',
            6: 'https://a7a7.net/meitu/index.php/category/zhaiwu/#cate_zhaiwu',
            7: 'https://a7a7.net/meitu/index.php/category/mmd/#cate_mmd',
            8: 'https://a7a7.net/meitu/index.php/category/zhaiwu/',
            9: 'https://a7a7.net/meitu/index.php/bq.html'
            }
    for link in itmes:
        piclink = link.get('href')  # 获取链接
        str2.append(piclink)  # 加入列表
    for i in str2:
        for s in str4.values():
            if i == s:
                str2.remove(s)
                #print('已处理链接')
    str2.reverse()
    return str2

def api2():
    list1 = []
    list1.extend(api())
    url = list1[0]
    re = requests.get(url, verify=False)
    soup = BeautifulSoup(re.content, 'html.parser')
    for i in soup.find_all('img'):
        itmes = i.get('data-original')
    return itmes,list1,i

num1,num2,num3 = api2()
print(num1)
print(num2)
print(num3)
# for s in range(1,101):
#     print(api2())

# for i in range(1,100):
#     print(api())

path = "d:/pic/"

def baocun():
    for index, item in enumerate(api2()):
        if item:
            html = requests.get(api2())  # get函数获取图片链接地址，requests发送访问请求
            str2 = random.randrange(999999)
            img_name = path + str(index + str2) + '.jpg'
            with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
                file.write(html.content)
                file.flush()
            file.close()  # 关闭文件
            print('第%d张图片下载完成' % (index + str2))
            time.sleep(1)  # 自定义延时



while True:
    try:
        baocun()
    except BaseException as b:
            print(b)
            print('抓取完成')

