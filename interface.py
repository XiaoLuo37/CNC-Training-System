# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 981, 741))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_code = QtWidgets.QFrame(self.frame)
        self.frame_code.setGeometry(QtCore.QRect(380, 20, 591, 611))
        self.frame_code.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_code.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_code.setObjectName("frame_code")
        self.textEdit = QtWidgets.QTextEdit(self.frame_code)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 551, 511))
        self.textEdit.setStyleSheet(".QTextEdit{\n"
"    background-color: rgb(222, 221, 218);\n"
"    color: rgb(36, 31, 49);\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_code)
        self.stackedWidget_3.setGeometry(QtCore.QRect(30, 10, 521, 61))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_right = QtWidgets.QLabel(self.page_9)
        self.label_right.setGeometry(QtCore.QRect(210, 20, 131, 31))
        self.label_right.setStyleSheet("color: rgb(51, 209, 122);\n"
"font: 18pt \"Noto Sans Brahmi\";")
        self.label_right.setObjectName("label_right")
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_error = QtWidgets.QLabel(self.page_8)
        self.label_error.setGeometry(QtCore.QRect(210, 20, 131, 31))
        self.label_error.setStyleSheet("color: rgb(224, 27, 36);\n"
"font: 18pt \"Noto Sans Brahmi\";")
        self.label_error.setObjectName("label_error")
        self.stackedWidget_3.addWidget(self.page_8)
        self.frame_id = QtWidgets.QFrame(self.frame)
        self.frame_id.setGeometry(QtCore.QRect(20, 20, 351, 611))
        self.frame_id.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_id.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_id.setObjectName("frame_id")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_id)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 20, 331, 581))
        self.stackedWidget.setStyleSheet(".QPushButton{\n"
"    border: none;\n"
"    font: 14pt \"Noto Sans Brahmi\";\n"
"    background-color: rgb(246, 245, 244);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 191, 261))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pictures/Source/guo.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 340, 251, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_6 = QtWidgets.QLabel(self.page_10)
        self.label_6.setGeometry(QtCore.QRect(70, 40, 191, 261))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/pictures/Source/zhang.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_10)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 340, 251, 231))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.stackedWidget.addWidget(self.page_10)
        self.frame_cue = QtWidgets.QFrame(self.frame)
        self.frame_cue.setGeometry(QtCore.QRect(19, 639, 951, 91))
        self.frame_cue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cue.setObjectName("frame_cue")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_cue)
        self.stackedWidget_2.setGeometry(QtCore.QRect(19, 10, 921, 71))
        self.stackedWidget_2.setStyleSheet(".QPushButton{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(222, 221, 218);\n"
"}\n"
".QPushButton:pressed{\n"
"    padding-top: 3px;\n"
"    padding-left: 3px;\n"
"}\n"
".QLabel{\n"
"    color: rgb(237, 51, 59);\n"
"    font: 20pt \"Noto Sans Brahmi\";\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 631, 51))
        self.label_5.setObjectName("label_5")
        self.Button0 = QtWidgets.QPushButton(self.page_3)
        self.Button0.setGeometry(QtCore.QRect(730, 10, 151, 51))
        self.Button0.setObjectName("Button0")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_2 = QtWidgets.QLabel(self.page_4)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 421, 51))
        self.label_2.setObjectName("label_2")
        self.Button1 = QtWidgets.QPushButton(self.page_4)
        self.Button1.setGeometry(QtCore.QRect(740, 10, 151, 51))
        self.Button1.setObjectName("Button1")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label = QtWidgets.QLabel(self.page_5)
        self.label.setGeometry(QtCore.QRect(310, 10, 421, 51))
        self.label.setObjectName("label")
        self.Button2 = QtWidgets.QPushButton(self.page_5)
        self.Button2.setGeometry(QtCore.QRect(739, 10, 151, 51))
        self.Button2.setObjectName("Button2")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_3 = QtWidgets.QLabel(self.page_6)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 421, 51))
        self.label_3.setObjectName("label_3")
        self.Button3 = QtWidgets.QPushButton(self.page_6)
        self.Button3.setGeometry(QtCore.QRect(740, 10, 151, 51))
        self.Button3.setObjectName("Button3")
        self.stackedWidget_2.addWidget(self.page_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans Brahmi\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Please input G-code</span></p></body></html>"))
        self.label_right.setText(_translate("MainWindow", "正    确"))
        self.label_error.setText(_translate("MainWindow", "错    误"))
        self.pushButton.setText(_translate("MainWindow", "姓  名"))
        self.pushButton_2.setText(_translate("MainWindow", "小    郭"))
        self.pushButton_3.setText(_translate("MainWindow", "工  号"))
        self.pushButton_4.setText(_translate("MainWindow", "202215000207"))
        self.pushButton_5.setText(_translate("MainWindow", "姓  名"))
        self.pushButton_6.setText(_translate("MainWindow", "小    张"))
        self.pushButton_7.setText(_translate("MainWindow", "工  号"))
        self.pushButton_8.setText(_translate("MainWindow", "202201000730"))
        self.label_5.setText(_translate("MainWindow", "欢迎使用高真实感——三维模拟数控车床实训平台"))
        self.Button0.setText(_translate("MainWindow", "开    始"))
        self.label_2.setText(_translate("MainWindow", "请检查机床状态"))
        self.Button1.setText(_translate("MainWindow", "确    定"))
        self.label.setText(_translate("MainWindow", "请安装加工工件"))
        self.Button2.setText(_translate("MainWindow", "确    定"))
        self.label_3.setText(_translate("MainWindow", "请输入G代码"))
        self.Button3.setText(_translate("MainWindow", "开始加工"))
import Source_rc
