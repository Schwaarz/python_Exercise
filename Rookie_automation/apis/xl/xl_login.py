import base64
import calendar
import time
import requests
from Rookie_automation.apis.xl.init_value import host_url, username, password
from Rookie_automation.config.read_config import ReadConf


def login():
    init_value = ReadConf('D:\python\Rookie_automation\config\config.ini')
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    newtime = str(time_stamp) + "000"  # 时间戳+三个0
    bs = str(base64.b64encode(newtime.encode('utf-8')), "utf-8")  # 转码base64
    url = host_url + "admin/base/login?username=" + username + "&password=" + password + ""
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()
    token = result['data']['token']
    token2 = token + '%' + bs
    init_value.set_option("api_section", "token", token2)
    print(token2)

login()