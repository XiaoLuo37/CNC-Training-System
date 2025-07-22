import RPi.GPIO as GPIO  # 导入RPi.GPIO库并命名为GPIO

class DCMotor:
    def __init__(self, pin_direct1, pin_direct2, function):
        """
        初始化直流电机类
        :param pin_direct1: 直流电机方向引脚1
        :param pin_direct2: 直流电机方向引脚2
        :param function: 电机功能描述
        """
        self.pin_direct1 = pin_direct1  # 保存方向引脚1
        self.pin_direct2 = pin_direct2  # 保存方向引脚2
        self.function = function  # 保存电机功能描述
    
    def DCMotor_Enable(self):
        """
        启用直流电机，将方向引脚设置为输出模式
        """
        GPIO.setup(self.pin_direct1, GPIO.OUT)  # 设置方向引脚1为输出模式
        GPIO.setup(self.pin_direct2, GPIO.OUT)  # 设置方向引脚2为输出模式
    
    def DCMotor_run(self, struct):
        """
        控制直流电机运行
        :param struct: 控制信号，决定电机的运行方向
        """
        if struct == 2:
            # 设置方向引脚1为高电平，方向引脚2为低电平，电机正转
            GPIO.output(self.pin_direct1, GPIO.HIGH)
            GPIO.output(self.pin_direct2, GPIO.LOW)
        elif struct == 1:
            # 设置方向引脚1为低电平，方向引脚2为高电平，电机反转
            GPIO.output(self.pin_direct1, GPIO.LOW)
            GPIO.output(self.pin_direct2, GPIO.HIGH)
        else:
            # 设置方向引脚1和方向引脚2为低电平，电机停止
            GPIO.output(self.pin_direct1, GPIO.LOW)
            GPIO.output(self.pin_direct2, GPIO.LOW)