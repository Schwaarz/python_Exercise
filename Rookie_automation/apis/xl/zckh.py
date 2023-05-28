import json
from apis.xl.init_value import host_url,token
import requests
from faker import Faker
fake = Faker(locale='zh_CN')
url = host_url+"api/pc/tempCompany"

def zckh():
    payload = {
    "data": {
        "info": {
            "id": "",
            "name": "深圳红璞科技管理有限公司",
            "office_address": {
                "pac": [
                    "广东省",
                    "深圳市",
                    "福田区",
                    "福保街道"
                ],
                "detailed": ""+fake.street_address()+"",
                "address": "广东省深圳市福田区福保街道"+fake.street_address()+"",
                "province": "广东省",
                "city": "深圳市",
                "county": "福田区",
                "street": "福保街道"
            },
            "office_telephone": [
                "12222"
            ],
            "factory_address": [
                {
                    "pac": [
                        "广东省",
                        "深圳市",
                        "福田区",
                        "福保街道"
                    ],
                    "detailed": ""+fake.street_address()+"",
                    "address": "广东省深圳市福田区福保街道"+fake.street_address()+"",
                    "province": "广东省",
                    "city": "深圳市",
                    "county": "福田区",
                    "street": "福保街道"
                }
            ],
            "fax": [
                "122222222222222222222222222222"
            ],
            "remarks": "",
            "key_brand": 1,
            "is_different": 2,
            "potential_correlation": 2,
            "abbreviation": ""
        },
        "card": [
            {
                "card": "uploads/common/20230319/5a58a9fdcc70cbb17917d0c597aa6318.png",
                "corporate_name": "",
                "contacts": [
                    {
                        "value": ""
                    }
                ],
                "office_telephone": [
                    {
                        "value": ""
                    }
                ],
                "telephone": "",
                "fax": "",
                "factory_address": [
                    {
                        "value": ""
                    }
                ],
                "office_address": "",
                "relation": [
                    {
                        "value": ""
                    }
                ],
                "post": [
                    {
                        "value": ""
                    }
                ]
            }
        ],
        "contacts": [
            {
                "id": "",
                "full_name": "33",
                "telephone": "44",
                "post": 1
            }
        ],
        "relation": [],
        "pictures": [
            {
                "img": "uploads/common/20230319/1032ec21e9b674fff8e06178f443ada4.png",
                "type": 1
            },
            {
                "type": 2
            },
            {
                "type": 3
            },
            {
                "type": 4
            }
        ]
    }
}
    headers = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'http://120.79.34.175:8508',
  'Referer': 'http://120.79.34.175:8508/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
  'token': token
}
    payload = json.dumps(payload) # 转成JSON
    payload2 = json.loads(payload) #  使用json.loads 解码
    response = requests.request("POST", url, headers=headers, json=payload2)
    result = response.json()
    code = result["code"]
    return code
