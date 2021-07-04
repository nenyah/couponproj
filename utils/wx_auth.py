import json

import requests

AppSecret = 'fadbadb4ae6d64291b1f62a5d4e63d2e'
js_code = ''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
url = 'https://api.weixin.qq.com/sns/jscode2session?'


# 微信认证
def auth_code2session(js_code):
    params = {
        'appid': 'wx5e9dd7985ded64b1',
        'secret': AppSecret,
        'js_code': js_code,
        'grant_type': 'authorization_code'
    }
    res = requests.get(url, headers=headers, params=params, verify=True)

    res.encoding = 'utf-8'
    r_list = res.text
    j_list = json.loads(r_list)
    return j_list
