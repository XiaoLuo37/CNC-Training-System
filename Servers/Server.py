import time  # 导入时间库
import socket  # 导入socket库

from Define import *  # 从Define模块导入所有内容

from PyQt5.QtWidgets import *

# 服务器类
class Server:
    def __init__(self,textEdit: QTextEdit):
        self.textEdit = textEdit

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  # 创建一个TCP/IP套接字
        address = ('0.0.0.0', port)  # 绑定本地的IP和端口
        self.s.bind(address)  # 绑定套接字到地址
        self.s.listen(127)  # 设置最大连接数并开始监听

    def receive_all(self, conn, count):
        """
        接收指定长度的字节数据
        :param conn: 客户端连接
        :param count: 要接收的字节数
        :return: 接收到的字符串数据
        """
        buf = b''  # 初始化一个空的字节串
        while len(buf) < count:  # 当接收到的字节长度小于指定长度时继续接收
            recv_data_temp = conn.recv(count - len(buf))  # 接收剩余的字节数
            if not recv_data_temp:
                return None  # 如果没有接收到数据，返回None
            buf += recv_data_temp  # 将接收到的数据添加到缓冲区
        return buf.decode('utf-8')  # 将字节数据解码为字符串并返回
    
    def run(self):
        conn, addr = self.s.accept()  # 等待客户端连接
        print('connect from ' + str(addr))  # 打印客户端地址
        try:
            while True:
                recv_from_qt = self.receive_all(conn, recv_len)  # 接收指定长度的数据
                if recv_from_qt is None:
                    break  # 如果接收的数据为空，跳出循环
                print('recv_from_qt = ',recv_from_qt)
                if recv_from_qt in commands:
                    if recv_from_qt == 'inpu':
                        self.textEdit.setText(gcode)
                    else:
                        commands[recv_from_qt]()  # 根据接收到的命令执行相应的操作
                else:
                    print("Unknown command received")  # 如果收到的命令未知，提示信息
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()  # 关闭客户端连接
            self.close()  # 关闭服务器
            print("Server closed")

    # 关闭服务器
    def close(self):
        """
        关闭服务器
        """
        self.s.close()
        GPIO.cleanup()
