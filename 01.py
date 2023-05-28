import json

import requests
# 接口地址
url = 'http://172.16.2.81/frontend/api/login'
# 请求数据
data = {
        "username": "admin",
        "userpwd": "sxNShX5aXGZHvI+FzQPV5hkc/uiZj8iIccCzJ4Pm7IjVAam5iQ57Fn3oicyhGGQjE69qo04w8Wha9FxhXf6TFl0pl1ig0P6UXJFvpux5a9VTAWie2WkRU4nw7YiHbUGoxhmzdkhF8IftghqsbJD7MInaEd/WtPmiQcbBwiDE3RA="
        }
# 将请求数据转换为 json 格式
json_data = json.dumps(data)
# 设置请求头，指定请求体的数据格式为 json
headers = {'Content-Type': 'application/json;charset=UTF-8'}
# 发送 POST 请求
response = requests.post(url, data=json_data, headers=headers)
# 解析响应数据
result = response.json()
# 获取token
accesstoken = result['data']['accesstoken']
print(result)
print(accesstoken)
# 断言响应状态码和返回结果
assert response.status_code == 200
assert result['data']['orgid'] == '999000001'
assert result['data']['userdisplayname'] == 'Sirm管理员'

