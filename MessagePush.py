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
        textYujing = self.TextYuJing.toPlainText()
        if self.radioButton.isChecked():
            self.MessageDisplayContent.update1(textYujing)
        if self.radioButton_2.isChecked():
            self.MessageDisplayContent.update1(textYujing)



    def loggingRecordDisplay(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())