import sys
from PyQt5.QtCore import Qt, QTimer,QDateTime,QThread
from PyQt5.QtGui import QFont, QFontMetrics, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import ScrollTextWindow
from UI_MainWindow import  Ui_MainWindow
from MessageGenerate import MessageGenerateAndUpload as MGAU
import schedule
import time

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
        self.pushButton_yujing.clicked.connect(self.functionForYJButtonClick)
        #开启后台定时上传线程

        # self.thread = GenerateUploadThread()
        # self.thread.signal.connect(self.displayInBrowser)
        # self.thread.start()

    def dateTimeRefresh(self):
        currentDateTime = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.lcdNumber.display(currentDateTime)

    def funtionForYjTimeOut(self):
        self.yj_timer.stop()
        self.radioButton.setChecked(True)
        self.TextYuJing.setPlainText("")
        QMessageBox.information(self,"提示","预警发布模式已自动终止")

    def functionForYJButtonClick(self):
        if (self.radioButton_2.isChecked()) or (self.radioButton_3.isChecked()):
            self.ybyjMessagePushAndDisplayRefresh()
            timelast = float(self.lineEdit.text())
            self.yj_timer = QTimer()
            self.yj_timer.timeout.connect(self.funtionForYjTimeOut)
            self.yj_timer.start(timelast*3600*1000)#小时转毫秒
        else:
            QMessageBox.critical(self,"错误","当前模式不支持预警发布")

    def displayInBrowser(self,text1,text2):
        self.loggingBrowser.append(ybyj_log)
        self.MessageDisplayContent.update1(content_new)

    def ybyjMessagePushAndDisplayRefresh(self):
        ybyj_text = self.TextYuJing.toPlainText()
        if self.radioButton.isChecked():
            state = 0
        if self.radioButton_2.isChecked():
            state = 1
        if self.radioButton_3.isChecked():
            state = 2
        ybyj_log,content_new=MGAU().GenerateYBYJAndUpload(ybyj_text,state)
        self.loggingBrowser.append(ybyj_log)
        self.MessageDisplayContent.update1(content_new)


class GenerateUploadThread(QThread):
    signal = QtCore.pyqtSignal(str,str)
    def __init__(self,text,state):
        super(GenerateUploadThread,self).__init__()
        self.ybyj_text = text
        self.state = state

    def run(self):
        while True:
            nowtime = time.localtime()
            minute = time.strftime("%M",nowtime)
            time.sleep(1)
            ybyj_log, content_new = MGAU().GenerateYBYJAndUpload(self.ybyj_text,self.state)
            self.signal.emit(ybyj_log,content_new)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())