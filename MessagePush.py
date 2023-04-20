import sys
from PyQt5.QtCore import Qt, QTimer,QDateTime
from PyQt5.QtGui import QFont, QFontMetrics, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import ScrollTextWindow
from UI_MainWindow import  Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #文件路径基本信息
        #设置界面左上角logo
        self.LogoLabel.setPixmap(QtGui.QPixmap("镇江气象logo（圆）.png"))
        self.LogoLabel.setScaledContents(True)
        #时间控件刷新
        dateTimeTimer = QTimer(self)
        dateTimeTimer.timeout.connect(self.dateTimeRefresh)
        dateTimeTimer.start()
        #推送按钮触发响应机制
        self.pushButton_yujing.clicked.connect(self.messageDisplayRefresh)

    def getFromFTPStation(self):
        pass

    def pushToFTPStation(self):
        pass

    def dateTimeRefresh(self):
        currentDateTime = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.lcdNumber.display(currentDateTime)


    def messageDisplayRefresh(self):
        text="自提交入党申请书以来，我时刻注意锻炼和提升自己，努力在各方面尝试以一名合格党员的标准严格要求和审视自己。提交入党申请书的这一年多来，我始终将成为一名光荣的中国共产党员设定为我的人生目标之一。从去年12月至今，我在党组织的关心和帮助下不断进步和成长，充分认识到镇江市气象局党组织这个大家庭的团结和温暖，在此期间，我也努力改正和弥补自己的不足。在学习、工作和生活上严格按照党员的标准来要求自己，认真履行党员的义务，通过身边优秀党员同志的帮助以及自身努力不断充实和完善自己。"
        ScrollTextWindow.ScrollTextWindow.update(text)


    def loggingRecordDisplay(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())