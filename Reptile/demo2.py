import threading
import time
import requests
def fun_timer():
    ret = requests.get('https://api.66mz8.com/api/rand.tbimg.php',verify=False)
    response = requests.get(ret)

while True:
    timer = threading.Timer(5, fun_timer)#等待5s钟调用一次fun_timer() 函数
    timer.start()
    timer.join()