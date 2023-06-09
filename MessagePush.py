import sys
from PyQt5.QtCore import Qt ,QTime,QTimer,QDateTime,QThread
from PyQt5.QtGui import QFont, QFontMetrics, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import ScrollTextWindow
from UI_MainWindow import  Ui_MainWindow
from MessageGenerate import MessageGenerateAndUpload as MGAU
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #重启软件后自动重置logging日志
        self.loggingBrowser.setText("")
        #设置界面左上角logo
        self.LogoLabel.setPixmap(QtGui.QPixmap("镇江气象logo（圆）.png"))
        self.LogoLabel.setScaledContents(True)
        #时间控件刷新
        dateTimeTimer = QTimer(self)
        dateTimeTimer.timeout.connect(self.dateTimeRefresh)
        dateTimeTimer.start()
        #推送按钮click推送预警线程
        self.pushButton_yujing.clicked.connect(self.ybyj_button_click_upload_thread)
        #推送按钮click推送省局线程
        self.pushButton_jiangsu.clicked.connect(self.jsyb_button_click_upload_thread)
        #后台定时上传线程(每一分钟发出一次timeout信号)
        self.backUploadTimer = QTimer(self)
        self.backUploadTimer.timeout.connect(self.start_back_upload_thread)
        self.backUploadTimer.start(60000)


    # def get_how_long_to_25(self):
    #     self.now = QTime.currentTime()
    #     self.minutes_to_25 = abs(25 - self.now.second()%60)
    #     if self.minutes_to_25 == 0:
    #         self.minutes_to_25 = 60

    def get_ybyjtext_radiobuttonstate(self):
        self.ybyj_text = self.TextYuJing.toPlainText()
        #判断当前模式
        if self.radioButton.isChecked():
            self.state = 0
        if self.radioButton_2.isChecked():
            self.state = 1
        if self.radioButton_3.isChecked():
            self.state = 2

    def start_back_upload_thread(self):
        if QTime.currentTime().minute()==15:
            self.thread1 = GenerateUploadThread(self.ybyj_text,self.state)
            self.thread1.signal.connect(self.displayInBrowser)
            self.thread1.start()
        else:
            pass



    def ybyj_button_click_upload_thread(self):
        if self.state==1 or self.state==2:
            self.thread2 = YuJingUploadThread(self.ybyj_text,self.state)
            self.thread2.signal.connect(self.displayInBrowser)
            self.thread2.start()
            timelast = float(self.lineEdit.text())
            self.yj_timer = QTimer()
            self.yj_timer.timeout.connect(self.funtionForYjTimeOut)
            self.yj_timer.start(timelast *3600*1000)  # 小时转毫秒
        else:
            QMessageBox.critical(self, "错误", "当前模式不支持预警发布")


    def jsyb_button_click_upload_thread(self):
        pass


    def dateTimeRefresh(self):
        currentDateTime = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.lcdNumber.display(currentDateTime)
        self.get_ybyjtext_radiobuttonstate()
        # self.get_how_long_to_25()


    def funtionForYjTimeOut(self):
        self.yj_timer.stop()
        self.radioButton.setChecked(True)
        self.TextYuJing.setPlainText("")
        QMessageBox.information(self,"提示","预警发布模式已自动终止")

    # def functionForYJButtonClick(self):
    #     if (self.radioButton_2.isChecked()) or (self.radioButton_3.isChecked()):
    #         self.ybyjMessagePushAndDisplayRefresh()
    #         timelast = float(self.lineEdit.text())
    #         self.yj_timer = QTimer()
    #         self.yj_timer.timeout.connect(self.funtionForYjTimeOut)
    #         self.yj_timer.start(timelast*3600*1000)#小时转毫秒
    #     else:
    #         QMessageBox.critical(self,"错误","当前模式不支持预警发布")

    def displayInBrowser(self,text1,text2):
        self.loggingBrowser.append(text1)
        self.MessageDisplayContent.update1(text2)

    # def ybyjMessagePushAndDisplayRefresh(self):
    #     ybyj_text = self.TextYuJing.toPlainText()
    #     if self.radioButton.isChecked():
    #         state = 0
    #     if self.radioButton_2.isChecked():
    #         state = 1
    #     if self.radioButton_3.isChecked():
    #         state = 2
    #     ybyj_log,content_new=MGAU().GenerateYBYJAndUpload(ybyj_text,state)
    #     self.loggingBrowser.append(ybyj_log)
    #     self.MessageDisplayContent.update1(content_new)


class YuJingUploadThread(QThread):
    signal = QtCore.pyqtSignal(str, str)

    def __init__(self, text, state):
        super(YuJingUploadThread, self).__init__()
        self.ybyj_text = text
        self.state = state

    def run(self):
        ybyj_log, content_new = MGAU().GenerateYBYJAndUpload(self.ybyj_text, self.state)
        self.signal.emit(ybyj_log, content_new)

class GenerateUploadThread(QThread):
    signal = QtCore.pyqtSignal(str,str)
    def __init__(self,text1,text2):
        super(GenerateUploadThread,self).__init__()
        self.text1 = text1
        self.text2 = text2
    def run(self):
        # while True:
        #     nowtime = time.localtime()
        #     minute = time.strftime("%M",nowtime)
        #     print(minute)
        #     time.sleep(1)
        ybyj_log, content_new = MGAU().GenerateYBYJAndUpload(self.text1,self.text2)
        self.signal.emit(ybyj_log,content_new)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())