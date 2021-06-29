#  发请求，获取 access_token

import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
AK = 'xMUZoHQvtinZeSawFlUV6IIQ'
SK = 'iM10EYfc0LL0RoHR2nTzNxsH3EikWPkW'

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + f"{AK}" + '&client_secret=' + f"{SK}"

def get_accesstoken():
    print("host : " + host)
    print("正在获取access_token")
    response = requests.get(host)
    if response:
        res = response.json()
        print("access_token : " + res['access_token'])
        return res['access_token']
    else:
        print('请求失败')
        return False
