import requests
from PIL import Image
from io import BytesIO
import urllib3
import os
import threading
import ip
import seleniumsetu
import time
urllib3.disable_warnings()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64'
}
proxies = {
    'http': 'HTTP://183.64.239.19:8060'
}


def api():
    #  url = 'https://api.vvhan.com/api/tao'  # 请求接口并返回URL
    url = seleniumsetu.link()
    return url


def api2():
    ret = requests.get(api(), verify=False, proxies=proxies, headers=header)  # 关闭https证书警告
    str_1 = ret.headers['Ali-Swift-Global-Savetime']  # 拿到headers的eagleid存储在str_1中
    return str_1  # 返回str_1的值


def getimage(ret):  # 响应并返回值
    response = requests.get(ret)
    return response


def pic():  # 解析响应并返回图片数据
    try:  # 异常处理
        response = getimage(api())  # 使用响应函数处理请求函数并存储在response变量中
        image = Image.open(BytesIO(response.content))  # 二进制图片内容转换为图片
        return image
    except BaseException as a:
        print(a)    # 打印异常
        if pic() != None:
            pic()


def pic_cun():  # 循环给图片命名
    while True:
        if pic() != 'None':
            pic().save('d:/pic/' + api2() + '.png')  # 保存为Png格式
        try:
            pic().save(pic(), "JPEG")
        except AttributeError:
            print("Couldn't save image {}".format(pic()))
            pic().save('d:/pic/' + api2() + '.jpg')  # 异常处理，保存为JPG格式
for a in range(1,10):
    pic_cun()

def pic_name():
    path = r"d:/pic/"  # 图片路径
    num = 1
    for file in os.listdir(path):  # 遍历给图片重命名
        os.rename(os.path.join(path, file), os.path.join(path + str(num)) + '.png')
        num = num + 1

# while True:
#     timer = threading.Timer(5, api())  # 定时5秒访问函数
#     pic_cun()
#     try:
#         timer = threading.Timer(5, pic())   # 定时5秒访问函数
#         time.sleep(2)
#         pic_cun()
#     except BaseException as c:
#         print(c)
#     timer.start()
#     timer.join()

# pic_name()  # 调用图片重命名函数






