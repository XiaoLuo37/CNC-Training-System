from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QHostAddress

import interface
from Servers.Server import Server

import Define

import sys
import threading

import RPi.GPIO as GPIO

# class TcpServerThread(QObject):
#     data_received_signal = pyqtSignal(str)

#     def __init__(self):
#         super().__init__()

#     def run(self):
#         self.tcp_server = QTcpServer()
#         if not self.tcp_server.listen(QHostAddress.Any, Define.port):         # 端口号
#             print(f"服务器启动失败，错误：{self.tcp_server.errorString()}")
#             sys.exit(1)
#         self.tcp_server.newConnection.connect(self.handle_new_connection)

#         while True:
#             self.tcp_server.waitForNewConnection(-1) # 阻塞等待新连接，-1表示一直等
#             client_socket = self.tcp_server.nextPendingConnection()
#             if client_socket:
#                 self.read_data_from_client(client_socket)  
    
#     def handle_new_connection(self):  # 只要有新客户端连接就会被调用
#         while True:
#             client_socket = self.tcp_server.nextPendingConnection()
#             if client_socket is None:
#                 break
#             client_address = client_socket.peerAddress().toString()
#             print(f'connect successfully from {client_address}')
#             self.read_data_from_client(self,client_socket)
    
#     def read_data_from_client(self,client_socket):
#         stream = QDataStream(client_socket)
#         stream.setVersion(QDataStream.Qt_5_3)
#         while True:
#             if client_socket.bytesAvailable() >= 4:
#                 data = stream.readBytes()
#                 received_data = QByteArray(data).data().decode('utf-8')
#                 self.data_received_signal.emit(received_data)  #发射数据
#             else:
#                 break
    
class My_interface(QMainWindow):
    def __init__(self, function):
        super().__init__()
        self.function = function
        self.gcode = Define.gcode

        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.Location_center()
        self.Bind_Button()
        self.Init_Window()

        #检测刷卡
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Detect_NFC_Card)
        self.timer.start(1000)

        # #添加TCP字符显示
        # self.create_QLabel_TCP()

        # # QTcpServer相关
        # self.tcp_server_thread = TcpServerThread()

        # # 槽函数处理字符串
        # self.tcp_server_thread.data_received_signal.connect(self.on_data_received)
        # self.server_thread = threading.Thread(target=self.tcp_server_thread.run)
        # self.server_thread.start()

        # Server 自定义服务类
        self.tcp_server = Server(self.ui.textEdit)
        self.tcp_server_thread = threading.Thread(target=self.tcp_server.run)
        self.tcp_server_thread.start()

        self.click_install_cnt = 0

    # def on_data_received(self, data):  #在这里进行机床处理
    #     print(f'received_from_QServer = {data}')
    #     self.QLabel_TCP.setText(str(data))
    #     if data in Define.commands:
    #         Define.commands[data]()
    #     else:
    #         print(f'\t invalid_data = {data}')

    # def create_QLabel_TCP(self):
    #     self.QLabel_TCP = QLabel(self.ui.frame_code)
    #     self.QLabel_TCP.setObjectName("QLabel_TCP")
    #     self.QLabel_TCP.setGeometry(10,10,100,20)
    #     self.QLabel_TCP.setStyleSheet("color: black; font-size: 14pt;")
    #     layout = self.ui.frame_code.layout()
    #     if not layout:
    #         layout = QVBoxLayout(self.ui.frame_code)
    #     layout.addWidget(self.QLabel_TCP)

    def Location_center(self):
        my_center = QDesktopWidget().availableGeometry().center()
        x = my_center.x()
        y = my_center.y()
        old_x, old_y, width, height = self.frameGeometry().getRect()
        self.move(int(x - width/2), int(y - height/2))

    def Init_Window(self):
        self.click_install_cnt = 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        self.ui.textEdit.setText('')

    def Detect_NFC_Card(self):
        if GPIO.input(Define.detect_nfc) == GPIO.HIGH:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.Init_Window()
        if GPIO.input(Define.detect_nfc) == GPIO.LOW:
            self.ui.stackedWidget.setCurrentIndex(2)

    def Bind_Button(self):
        # Button0
        # getIndex = self.ui.stackedWidget.currentIndex()   #去掉条件直接绑定
        # if getIndex == 1:
        self.ui.Button0.clicked.connect(lambda: self.Button0_start())
        # Button1
        self.ui.Button1.clicked.connect(lambda: self.Button1_start())
        # Button2
        self.ui.Button2.clicked.connect(lambda: self.Button2_start())
        # Button3
        self.ui.Button3.clicked.connect(lambda: self.Button3_start())

    def Button0_start(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    def Button1_start(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)

    def Button2_start(self):
        self.click_install_cnt += 1
        if self.click_install_cnt > 2:
            self.click_install_cnt = 0
            self.ui.stackedWidget_3.setCurrentIndex(1)
            QTimer.singleShot(800,lambda: self.ui.stackedWidget_3.setCurrentIndex(0))

            self.ui.stackedWidget_2.setCurrentIndex(3)
            self.ui.textEdit.setText('please input G-code\n......')
        else:
            self.ui.stackedWidget_3.setCurrentIndex(2)
            QTimer.singleShot(800,lambda: self.ui.stackedWidget_3.setCurrentIndex(0))

    def Button3_start(self):
        self.ui.textEdit.setText(self.gcode)

