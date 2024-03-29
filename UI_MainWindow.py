# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessagePush.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QFontMetrics, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import ScrollTextWindow


# class Ui_MainWindow(QtWidgets.QMainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 610)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(181, 100, 461, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.TextArea = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.TextArea.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.TextArea.setContentsMargins(0, 0, 0, 0)
        self.TextArea.setObjectName("TextArea")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("方正小标宋简体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.TextArea.addWidget(self.label_6)
        self.TextYuJing = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.TextYuJing.setStyleSheet("background-color: rgb(160, 255, 182);")
        self.TextYuJing.setObjectName("TextYuJing")
        self.TextArea.addWidget(self.TextYuJing)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("方正小标宋简体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.TextArea.addWidget(self.label_7)
        self.TextJiangSu = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.TextJiangSu.setObjectName("TextJiangSu")
        self.TextArea.addWidget(self.TextJiangSu)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(650, 100, 130, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.ButtonArea = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.ButtonArea.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.ButtonArea.setContentsMargins(0, 0, 0, 0)
        self.ButtonArea.setObjectName("ButtonArea")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.ButtonArea.addWidget(self.label_8)
        self.pushButton_yujing = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_yujing.sizePolicy().hasHeightForWidth())
        self.pushButton_yujing.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255, 239))
        gradient.setColorAt(1.0, QtGui.QColor(160, 255, 182))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_yujing.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_yujing.setFont(font)
        self.pushButton_yujing.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 239), stop:1 rgba(160, 255, 182, 255));\n"
"\n"
"    border:1px solid #717171;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(118, 255, 149, 255), stop:1 rgba(160, 255, 182, 255));\n"
"    border:2px solid #717171;\n"
"    border-radius:10px\n"
"}")
        self.pushButton_yujing.setObjectName("pushButton_yujing")
        self.ButtonArea.addWidget(self.pushButton_yujing)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.ButtonArea.addWidget(self.label_9)
        self.pushButton_jiangsu = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_jiangsu.sizePolicy().hasHeightForWidth())
        self.pushButton_jiangsu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_jiangsu.setFont(font)
        self.pushButton_jiangsu.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 239), stop:1 rgba(188, 244, 255, 255));\n"
"\n"
"    border:1px solid #717171;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(188, 244, 255, 255));\n"
"    border:2px solid #717171;\n"
"    border-radius:10px\n"
"}")
        self.pushButton_jiangsu.setObjectName("pushButton_jiangsu")
        self.ButtonArea.addWidget(self.pushButton_jiangsu)
        with open(r'\\10.127.192.121\Data\fwb\Zjxsp\市台最新时次预报.txt','r+', encoding='gbk') as f:
            song = f.readline()
        songInfo = {
            'songName':song}
        self.MessageDisplayContent= ScrollTextWindow.ScrollTextWindow(songInfo["songName"],self)
        self.MessageDisplayContent.setGeometry(QtCore.QRect(179, 10, 598, 71))

        self.MessageDisplay = QtWidgets.QWidget(self.centralwidget)
        self.MessageDisplay.setGeometry(QtCore.QRect(175, 10, 601, 71))
        self.MessageDisplay.setStyleSheet("border:3px solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(172, 172, 172, 255));")
        self.MessageDisplay.setObjectName("MessageDisplay")
        self.verticalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_3.setGeometry(QtCore.QRect(10, 140, 161, 181))
        self.verticalWidget_3.setStyleSheet("border:1px solid")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget_3)
        font = QtGui.QFont()
        font.setFamily("方正小标宋简体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.verticalWidget_3)
        self.line.setStyleSheet("border:none")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.radioButton = QtWidgets.QRadioButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("border:none")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("border:none")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)

        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("border:none")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)


        self.widget = QtWidgets.QWidget(self.verticalWidget_3)
        self.widget.setStyleSheet("border:none")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:0px solid")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(5, 80, 161, 50))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setStyleSheet("border:none;color: pink")
        self.loggingBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.loggingBrowser.setGeometry(QtCore.QRect(15, 360, 761, 221))
        self.loggingBrowser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(172, 172, 172, 255));\n"
"border:2px solid;")
        self.loggingBrowser.setObjectName("loggingBrowser")
        # self.line_4 = QtWidgets.QFrame(self.centralwidget)
        # self.line_4.setGeometry(QtCore.QRect(10, 90, 771, 16))
        # self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 330, 91, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 330, 321, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(450, 330, 321, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(10, 10, 166, 71))
        self.horizontalGroupBox.setStyleSheet("border:none")
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.LogoLabel = QtWidgets.QLabel(self.horizontalGroupBox)
        self.LogoLabel.setGeometry(QtCore.QRect(8, 2, 65, 61))
        self.LogoLabel.setStyleSheet("border:none")
        self.LogoLabel.setText("")
        self.LogoLabel.setObjectName("LogoLabel")
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalGroupBox)
        self.verticalWidget_4.setGeometry(QtCore.QRect(80, 0, 91, 60))
        self.verticalWidget_4.setStyleSheet("border:none")
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("border:none")
        self.label_2.setLineWidth(2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "气象服务短信显示推送软件"))
        self.label_6.setText(_translate("MainWindow", "镇江预报预警信息："))
        self.label_7.setText(_translate("MainWindow", "省台预报信息："))
        self.pushButton_yujing.setText(_translate("MainWindow", "预警推送"))
        self.pushButton_jiangsu.setText(_translate("MainWindow", "省台推送"))
        self.label.setText(_translate("MainWindow", "预警信息推送设置"))
        self.radioButton.setText(_translate("MainWindow", "预报独立显示"))
        self.radioButton_2.setText(_translate("MainWindow", "预警独立显示"))
        self.radioButton_3.setText(_translate("MainWindow", "预报预警联合"))
        self.label_4.setText(_translate("MainWindow", "预警时长"))
        self.lineEdit.setText(_translate("MainWindow", "3"))
        self.label_5.setText(_translate("MainWindow", "小时"))
        self.loggingBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">rom PyQt5 import QtCore, QtGui, QtWidgets</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">import sys</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">#*************************通过ui文件转换得到的python代码**********************************</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">class Ui_Form(object):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    def setupUi(self, Form):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        Form.setObjectName(&quot;Form&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        Form.resize(400, 300)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label = QtWidgets.QLabel(Form)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setGeometry(QtCore.QRect(160, 80, 51, 51))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setStyleSheet(&quot;background-color: rgb(58, 111, 50);\\n&quot;&quot;border-radius: 25px; border:\\n&quot;&quot; 3px groove gray;border-style: outset;&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setText(&quot;&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setObjectName(&quot;label&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton1 = QtWidgets.QPushButton(Form)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton1.setGeometry(QtCore.QRect(150, 170, 75, 23))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton1.setObjectName(&quot;pushButton&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton2 = QtWidgets.QPushButton(Form)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton2.setGeometry(QtCore.QRect(150, 210, 75, 23))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton2.setObjectName(&quot;pushButton2&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.retranslateUi(Form)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        QtCore.QMetaObject.connectSlotsByName(Form)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    def retranslateUi(self, Form):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        _translate = QtCore.QCoreApplication.translate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        Form.setWindowTitle(_translate(&quot;Form&quot;, &quot;指示灯&quot;))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton1.setText(_translate(&quot;Form&quot;, &quot;开灯&quot;))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton2.setText(_translate(&quot;Form&quot;, &quot;关灯&quot;))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">#*************************功能实现代码**********************************</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">#自定义一个类，继承上面的类，来生成一个界面</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">class MyWindow(QtWidgets.QWidget,Ui_Form):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    def __init__(self):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        super(MyWindow,self).__init__()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.setupUi(self)  # 生成界面</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton1.clicked.connect(self.open_light)   # 按钮1连接到函数 open_light()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.pushButton2.clicked.connect(self.close_light)  # 按钮2连接到函数 close_light()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    # 开灯（改变标签背景为高亮的颜色）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    def open_light(self):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setStyleSheet(\'\'\'QLabel{background-color: rgb(0, 234, 0);border-radius: 25px; border: 3px groove gray;border-style: outset;}\'\'\')</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    # 关灯（改变标签背景为比较暗的颜色）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    def close_light(self):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        self.label.setStyleSheet(\'\'\'QLabel{background-color: rgb(58, 111, 50);border-radius: 25px; border: 3px groove gray;border-style: outset;}\'\'\')</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">if __name__==&quot;__main__&quot;:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    app = QtWidgets.QApplication(sys.argv)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    myshow = MyWindow()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    myshow.show()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    sys.exit(app.exec_())</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">————————————————</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">版权声明：本文为CSDN博主「今天是周日啊」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">原文链接：https://blog.csdn.net/m0_60037214/article/details/128161778</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "logging日志"))
        self.label_2.setText(_translate("MainWindow", "实 时"))
        self.label_3.setText(_translate("MainWindow", "显 示"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())