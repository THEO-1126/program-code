# 主窗口界面

import sys

import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPixmap, QIcon

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QApplication, QPushButton

from function import Child_IC

# 读取Qss文件
class ReadQss:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

styleFile = 'KeChengSheJi/CourseDesign/style.qss'
qssStyle = ReadQss.readQss(styleFile)


class main_App(QMainWindow):
    def __init__(self):
        super().__init__()
        # 标记是否已经打开图片
        self.isopen = False
        # 标记是否已经返回识别结果信息
        self.hasIdentify=False

    # 设置主窗口窗口
    def main_Ui(self, mainwindow):
        mainwindow.setFixedSize(1000, 700)
        mainwindow.setWindowTitle("图片识别")
        mainwindow.setWindowIcon(QIcon("KeChengSheJi/CourseDesign/pic/图片识别.png"))
        mainwindow.setObjectName("mainwindow")
        mainwindow.setStyleSheet(qssStyle)
        self.Ui(mainwindow)

    # 界面内容
    def Ui(self, mainwindow):
        # 识别类型
        self.widget1 = QtWidgets.QWidget(mainwindow)
        self.typeselect = QtWidgets.QLabel(self.widget1)
        self.typeselect.setText("选择识别类型")
        self.typeselect.setObjectName("typeselect")
        self.typeselect.setStyleSheet(qssStyle)
        self.typeselect.setFixedSize(120, 40)
        self.widget1.setGeometry(QtCore.QRect(70, 50, 350, 41))
        # 识别类型的组合框
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet(qssStyle)
        self.comboBox.setFixedSize(180, 40)
        self.comboBox.addItems(['通用物体和场景识别','动物识别', '植物识别', 'logo识别','果蔬识别','菜品识别','红酒识别','货币识别','地标识别'])
        # 识别类型和组合框的水平布局
        self.HBoxLayout1 = QtWidgets.QHBoxLayout(self.widget1)
        self.HBoxLayout1.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout1.addWidget(self.typeselect)
        self.HBoxLayout1.addWidget(self.comboBox)


        # 选择文件夹按钮
        self.widget2 = QtWidgets.QWidget(mainwindow)
        self.fileselect = QtWidgets.QPushButton(self.widget2)
        self.fileselect.setObjectName("fileselect")
        self.fileselect.setStyleSheet(qssStyle)
        self.fileselect.setFixedSize(150, 40)
        self.fileselect.setText("点击打开文件夹")
        self.widget2.setGeometry(QtCore.QRect(70, 110, 500, 50))
        self.fileselect.clicked.connect(self.openfile)
        self.pictext = QtWidgets.QLabel(self.widget2)
        self.pictext.setText("请选择文件夹")
        self.pictext.setObjectName("pictext")
        self.pictext.setStyleSheet(qssStyle)
        # 选择文件夹按钮和提示的水平布局
        self.HBoxLayout2 = QtWidgets.QHBoxLayout(self.widget2)
        self.HBoxLayout2.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout2.addWidget(self.fileselect)
        self.HBoxLayout2.addWidget(self.pictext)

        # 图片显示
        self.image = QtWidgets.QLabel(mainwindow)
        self.image.setGeometry(QtCore.QRect(70, 180, 500, 450))
        self.image.setObjectName("image")
        self.image.setStyleSheet(qssStyle)
        self.imagetext = QtWidgets.QLabel(self.image)
        self.imagetext.setText("图   片")
        self.imagetext.setObjectName("imagetext")
        self.imagetext.setStyleSheet(qssStyle)
        self.imagetext.setGeometry(QtCore.QRect(170, 0, 500, 450))

        # 三个按钮
        # 识别按钮
        self.widget3 = QtWidgets.QWidget(mainwindow)
        self.widget3.setGeometry(QtCore.QRect(630, 590, 300, 50))
        self.submitbutton = QtWidgets.QPushButton(self.widget3)
        self.submitbutton.setFixedSize(100, 40)
        self.submitbutton.setText("识 别")
        self.submitbutton.setObjectName("submitbutton")
        self.submitbutton.setStyleSheet(qssStyle)
        self.submitbutton.clicked.connect(self.resultshow)

        # 重置按钮
        self.resetbutton = QtWidgets.QPushButton(self.widget3)
        self.resetbutton.setFixedSize(90, 40)
        self.resetbutton.setText("重 置")
        self.resetbutton.setObjectName("resetbutton")
        self.resetbutton.setStyleSheet(qssStyle)
        self.resetbutton.clicked.connect(self.reset)

        # 关闭按钮
        self.exitbutton = QtWidgets.QPushButton(self.widget3)
        self.exitbutton.setFixedSize(90, 40)
        self.exitbutton.setText("关闭")
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.setStyleSheet(qssStyle)
        self.exitbutton.clicked.connect(self.exit)

        # 按钮的水平布局
        self.HBoxLayout3 = QtWidgets.QHBoxLayout(self.widget3)
        self.HBoxLayout3.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout3.addWidget(self.submitbutton)
        self.HBoxLayout3.addWidget(self.resetbutton)
        self.HBoxLayout3.addWidget(self.exitbutton)

        # 识别结果
        self.result = QtWidgets.QLabel(mainwindow)
        self.result.setGeometry(QtCore.QRect(630, 180, 300, 390))
        self.result.setObjectName("result")
        self.result.setStyleSheet(qssStyle)
        self.resulttext = QtWidgets.QTextEdit(self.result)
        self.resulttext.setObjectName("resulttext")
        self.resulttext.setStyleSheet(qssStyle)
        self.resulttext.setText("\n  识别结果显示：\n\n\n\n\n         选择识别类型及图片后\n\n         点击“确定”")
        self.resulttext.setReadOnly(True)
        self.resulttext.setGeometry(QtCore.QRect(1, 1, 298, 388))

    # 打开图片文件
    def openfile(self):
        self.fname = QFileDialog.getOpenFileName(self.widget2, "选择要识别的图片", "/", "Image Files(*.jpg;*.png)")
        if not self.fname[0].strip():
            pass
        else:
            self.isopen = True
            # 若点击识别按钮后图片说明未隐藏，则将其隐藏，并建立单行文本框
            if not self.pictext.isHidden():
                self.pictext.setHidden(True)
                self.picname = QtWidgets.QLineEdit(self.widget2)
                self.picname.setObjectName("picname")
                self.picname.setStyleSheet(qssStyle)
            # 先将单行文本框清空，再显示选择的文件路径
            self.picname.clear()
            self.picname.setText(self.fname[0])
            self.picname.setReadOnly(True)
            self.HBoxLayout2.addWidget(self.picname)
            # 将图片说明隐藏
            if not self.imagetext.isHidden():
                self.imagetext.setHidden(True)
            # 显示图片
            pixmap = QPixmap(self.fname[0])
            self.image.setPixmap(pixmap.scaled(QtCore.QSize(500, 450)))

    # 点击识别按钮后触发的事件
    def resultshow(self):
        # 获取组合框的索引值
        typenumber = self.comboBox.currentIndex()
        # 若未打开图片就点击确认按钮,弹出提示窗口
        if self.isopen == False:
            self.replyWindow = QtWidgets.QMessageBox(mainwindow)
            self.replyWindow.setWindowTitle("提示")
            self.replyWindow.setText("   请先选择图片")
            self.replyWindow.setWindowIcon(QIcon("KeChengSheJi/CourseDesign/pic/提示.png"))
            self.replyWindow.setIconPixmap(QPixmap("KeChengSheJi/CourseDesign/pic/提示 (1).png").scaled(30, 30))
            self.replyWindow.setObjectName("replyWindow")
            self.replyWindow.setStyleSheet(qssStyle)
            self.replyWindow.show()
        else:
            # 建立Child_IC()类的一个对象
            self.child_ic = Child_IC()
            # 发起请求后返回的识别结果
            resultconnect = self.child_ic.autonumber(typenumber, self.fname[0])
            if not resultconnect:
                self.resulttext.setText("\n\n识别结果显示：\n\n\n\t发送的请求响应失败")
            else:
                # 清除识别结果提示信息后，再显示返回的识别结果信息
                self.hasIdentify = True
                self.resulttext.clear()
                self.resulttext.setText("\n识别结果显示：")
                for key, value in resultconnect.items():
                    print(key + " : " + str(value))
                    self.resulttext.append("\n" + key + " : " + str(value))

    # 点击重置按钮后触发的事件
    def reset(self):
        if self.isopen:
            self.image.clear()
            self.imagetext.setHidden(False)
            self.picname.setHidden(True)
            self.pictext.setHidden(False)
        if self.hasIdentify:
            self.resulttext.clear()
            self.resulttext.setText("\n  识别结果显示：\n\n\n\n\n         选择识别类型及图片后\n\n         点击“确定”")

    # 点击关闭按钮后触发的事件
    def exit(self):
        # 点击关闭按钮后提示是否要关闭窗口
        self.closeWindow = QtWidgets.QMessageBox(mainwindow)
        self.okbtn =QtWidgets.QPushButton(QObject.tr(self,"确定"))
        self.okbtn.setObjectName("okbtn")
        self.okbtn.setStyleSheet(qssStyle)
        self.canclebtn = QtWidgets.QPushButton(QObject.tr(self, "取消"))
        self.canclebtn.setObjectName("canclebtn")
        self.canclebtn.setStyleSheet(qssStyle)
        self.closeWindow.addButton(self.okbtn,QMessageBox.AcceptRole)
        self.closeWindow.addButton(self.canclebtn, QMessageBox.RejectRole)
        self.closeWindow.setWindowTitle("提示")
        self.closeWindow.setText("    确定退出程序？")
        self.closeWindow.setWindowIcon(QIcon("KeChengSheJi/CourseDesign/pic/提示.png"))
        self.closeWindow.setIconPixmap(QPixmap("KeChengSheJi/CourseDesign/pic/提示 (1).png").scaled(30, 30))
        self.closeWindow.setObjectName("closeWindow")
        self.closeWindow.setStyleSheet(qssStyle)
        self.closeWindow.show()
        # 点击确定按钮后关闭整个程序
        self.okbtn.clicked.connect(mainwindow.close)


if __name__ == '__main__':
    # 使用Qt的GUI应用程序，每个qt项目必须先创建一个QApplication对象
    app = QApplication(sys.argv)
    # 实例化窗口
    mainwindow = QMainWindow()
    test = main_App()
    test.main_Ui(mainwindow)
    mainwindow.show()
    # 使用exit()时，主函数就会终止，sys.exit()确保干净利落不留痕迹地退出，关闭窗口后，进程退出
    sys.exit(app.exec_())
