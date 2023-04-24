import sys
from PyQt5.QtCore import Qt, QTimer,QDateTime
from PyQt5.QtGui import QFont, QFontMetrics, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import ScrollTextWindow
from UI_MainWindow import  Ui_MainWindow
from MessageGenerate import MessageGenerateAndUpload as MGAP
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

        schedule.every().minute.do(self.ybyjMessagePushAndDisplayRefresh)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def dateTimeRefresh(self):
        currentDateTime = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.lcdNumber.display(currentDateTime)

    def funtionForYjTimeOut(self):
        self.yj_timer.stop()
        self.radioButton.setChecked(True)
        self.TextYuJing.setPlainText("")
        QMessageBox.information(self,"提示","预警模式已终止")


    def functionForYJButtonClick(self):
        if (self.radioButton_2.isChecked()) or (self.radioButton_3.isChecked()):
            timelast = float(self.lineEdit.text())
            self.yj_timer = QTimer()
            self.yj_timer.timeout.connect(self.funtionForYjTimeOut)
            self.yj_timer.start(timelast*3600*1000)#小时转毫秒
        else:
            QMessageBox.critical(self,"错误","请手动切换到预警模式")


    def ybyjMessagePushAndDisplayRefresh(self):
        ybyj_text = self.TextYuJing.toPlainText()
        if self.radioButton.isChecked():
            state=0
        if self.radioButton_2.isChecked():
            state=1
        if self.radioButton_3.isChecked():
            state = 2

        ybyj_log,content_new=MGAP().GenerateYBYJAndUpload(ybyj_text,state)
        self.loggingBrowser.append(ybyj_log)
        self.MessageDisplayContent.update1(content_new)

Class GenerateUploadThread(QThread):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())