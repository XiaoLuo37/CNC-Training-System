import RPi.GPIO as GPIO  # 导入RPi.GPIO库并命名为GPIO
import serial  # 导入串口通信库
import time  # 导入时间库

# 将 Define 模块中的所有公共名称直接导入到当前模块的命名空间中
from Define import *

class Serial:
    def __init__(self, TXD, RXD, SERIAL):
        """
        初始化串口类
        :param TXD: 串口发送引脚
        :param RXD: 串口接收引脚
        :param SERIAL: 串口对象
        """
        self.TXD = TXD  # 发送引脚
        self.RXD = RXD  # 接收引脚
        self.ser = SERIAL  # 串口对象
        self.step = 0  # 步骤标志位
    
    def Send_to_Pico(self, data):
        """
        发送数据到Pico
        :param data: 要发送的数据
        """
        data = data.encode('utf-8')  # 将数据编码为UTF-8格式
        if self.step == 1:
            self.ser.write(data)  # 通过串口发送数据
            time.sleep(0.5)  # 等待0.5秒
    
    def Received_from_Pico(self):
        """
        从Pico接收数据
        """
        while True:
            if Serial_list[0].ser.in_waiting > 0:  # 检查是否有数据等待接收
                incoming_data = Serial_list[0].ser.readline().decode('utf-8').rstrip()  # 读取并解码数据
                print(f'Received: {incoming_data}')  # 打印接收到的数据