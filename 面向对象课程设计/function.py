# 识别类型的方法

import base64

import requests
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox

from request import get_accesstoken



class Child_IC(QWidget):
    def __init__(self):
        super().__init__()
        self.access_token = get_accesstoken()

    def autonumber(self, number, filename):
        if not self.access_token:
            self.replyerror.setWindowTitle("提示")
            self.replyerror.setText("发送请求失败\n详细信息：获取access_token失败")
            self.replyerror.setWindowIcon(QIcon("KeChengSheJi/CourseDesign/pic/提示.png"))
            self.replyerror.setIconPixmap(QPixmap("KeChengSheJi/CourseDesign/pic/提示 (1).png").scaled(30, 30))
            self.replyerror.setObjectName("replyerror")
            self.replyerror.show()
        elif number == 0:
            return self.advanced_general(filename)
        elif number == 1:
            return self.animal(filename)
        elif number == 2:
            return self.plant(filename)
        elif number == 3:
            return self.logo(filename)
        elif number == 4:
            return self.ingredient(filename)
        elif number == 5:
            return self.dish(filename)
        elif number == 6:
            return self.redwine(filename)
        elif number == 7:
            return self.currency(filename)
        elif number == 8:
            return self.landmark(filename)


    #  通用物体和场景识别高级版
    def advanced_general(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # 动物
    def animal(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # 植物
    def plant(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # logo
    def logo(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # 果蔬识别
    def ingredient(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # 菜品识别
    def dish(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    #  红酒识别
    def redwine(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    #  货币识别
    def currency(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/currency"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)


    #  地标识别
    def landmark(self, filename):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" +  self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        return self.response_judge(response)

    # 请求响应判断
    def response_judge(self,response):
        if response:
            print(response.json())
            connect = response.json()['result']
            if type(connect).__name__ == 'list':
                return connect[0]
            if type(connect).__name__ == "dict":
                return connect
        else:
            self.reply = QMessageBox.about(self, "提示", "请求响应失败")
            connect = False
        return connect
