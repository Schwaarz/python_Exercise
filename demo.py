import datetime
import time
from io import BytesIO

import requests
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from PIL import Image
urllib3.disable_warnings()
def timedTask():
    #print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    ret=requests.get('https://api.66mz8.com/api/rand.tbimg.php',verify=False)
    return ret

if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(timedTask, 'interval', seconds=2)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())


        def getimage(ret):  # 响应请求的数据并返回
            response = requests.get(ret)
            return response


        response = getimage(timedTask())
        image = Image.open(BytesIO(response.content))  # 转为图片

        num = ["1", "2", "3"]
        for i in range(len(num)):
            image.save('d:/pic/' + num[i] + '.png')

        time.sleep(5)


