import requests
from PIL import Image
from io import BytesIO
import urllib3
import os
import threading

urllib3.disable_warnings()



def api():
    url = 'https://api.vvhan.com/api/tao'  # 请求接口并返回URL
    return url


def api2():
    ret = requests.get(api(), verify=False)  # 关闭https证书警告
    str_1 = ret.headers['x-nws-log-uuid']  # 拿到headers的x-new-log-uuid存储在str_1中
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


def pic_cun():  # 循环给图片命名
    while True:
        try:
            pic().save('d:/pic/' + api2() + '.Png')  # 保存为Png格式
        except BaseException as b:
            print(b)
            pic().save('d:/pic/' + api2() + '.jpg')  # 异常处理，保存为JPG格式


def pic_name():
    path = r"d:/pic/"  # 图片路径
    num = 1
    for file in os.listdir(path):  # 遍历给图片重命名
        os.rename(os.path.join(path, file), os.path.join(path + str(num)) + '.png')
        num = num + 1


while True:
    timer = threading.Timer(5, api())  # 定时5秒访问函数
    try:
        timer = threading.Timer(5, pic())   # 定时5秒访问函数
    except BaseException as c:
        print(c)
        pic()   # 异常处理，无须定时即可访问
    pic_cun()   # 调用保存图片函数
    timer.start()
    timer.join()
# pic_name()  # 调用图片重命名函数






