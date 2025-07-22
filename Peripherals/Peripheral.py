from RedSensors.RedSensor import RedSensor                    # 从RedSensors.RedSensor模块导入RedSensor类
from Stepmotors.StepMotor import StepMotor                    # 从Stepmotors.StepMotor模块导入StepMotor类
#from Serials.Serial import Serial                            # 从Serials.Serial模块导入Serial类
from PushRods.PushRod import PushRod
from PressSensors.PressSensor import PressSensor
from MagnetSensors.MagnetSensor import MagnetSensor
import serial                                                 # 导入串口通信库
from Define import *                                          # 从Define模块导入所有内容
from Controlls.Control import Control

class Peripheral:
    def __init__(self):
        """
        初始化外设类
        """
        self.Init_Peripheral()                                # 调用初始化外设方法
    
    def Init_Peripheral(self):
        """
        初始化外设，包括步进电机、直流电机、红外传感器和串口
        """
        StepMotor_len = len(StepMotor_dict)                   # 获取步进电机字典的长度
        for key, value in StepMotor_dict.items():
            # 初始化步进电机对象
            key = StepMotor(pin_motor=value[0], pin_direct=value[1], pul=PUL, frequency_list=frequency_list, function='StepMotor')
            key.StepMotor_Enable(pwm_mark=StepMotor_len)      # 启用步进电机
            StepMotor_len -= 1                                # 步进电机数量减1
            StepMotor_list.append(key)                        # 将步进电机对象添加到列表中
        print('len(StepMotor) = %d' % (len(StepMotor_list)))  # 打印步进电机的数量
        
        # for key, value in DCMotor_dict.items():
        #     # 初始化直流电机对象
        #     key = DCMotor(value[0], value[1], 'DCMotor')
        #     key.DCMotor_Enable()  # 启用直流电机
        #     DCMotor_list.append(key)  # 将直流电机对象添加到列表中
        # print('len(DCMotor) = %d' % (len(DCMotor_list)))  # 打印直流电机的数量

        for key,value in PushRod_dict.items():
            # 初始化电推杆对象
            key = PushRod(pin_l=value[0],pin_r=value[1],function='PushRod')
            key.PushRod_Enable()
            PushRod_list.append(key)
        print('len(PushRod) = %d '%(len(PushRod_list)))
        
        for key, value in RedSensor_dict.items():
            # 初始化红外传感器对象
            key = RedSensor(value, 'RedSensor')
            key.RedSensor_Enable()  # 启用红外传感器
            RedSensor_list.append(key)  # 将红外传感器对象添加到列表中
        print('len(RedSensor) = %d' % (len(RedSensor_list)))  # 打印红外传感器的数量

        for key,value in PressSensor_dict.items():
            # 初始化压力传感器对象
            key = PressSensor(pin_sensor=value,function='PressSensor')
            key.PressSensor_Enable()
            PressSensor_list.append(key)
        print('len(PressSensor) = %d'%(len(PressSensor_list)))

        # for key,value in MagnetSensor_dict.items():
        #     # 初始化磁感应开关对象
        #     key = MagnetSensor(pin_sensor=value,function='MagnetSensor')
        #     key.MagnetSensor_Enable()
        #     MagnetSensor_list.append(key)
        # print('len(MagnetSensor) = %d'%(len(MagnetSensor_list)))

        #临时给nfc使用
        GPIO.setup(detect_nfc, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        My_Control = Control(function='Control',StepMotor_list=StepMotor_list,RedSensor_list=RedSensor_list,PushRod_list=PushRod_list)
        Control_list.append(My_Control)
        print('len(Control_list) = %d'%(len(Control_list)))
        
        # 初始化串口对象并添加到列表中
        #Serial_list.append(Serial(TXD=Serial_dict['TXD'], RXD=Serial_dict['RXD'], SERIAL=serial.Serial('/dev/ttyAMA0', 9600, timeout=0.8)))