import RPi.GPIO as GPIO  # 导入RPi.GPIO库并命名为GPIO
import time  # 导入时间库

class StepMotor:
    def __init__(self, pin_motor, pin_direct, pul, frequency_list, function):
        """
        初始化步进电机类
        :param pin_motor: 步进电机的脉冲引脚
        :param pin_direct: 步进电机的方向引脚
        :param pul: 脉冲数
        :param frequency_list: 频率列表
        :param function: 电机功能描述
        """
        self.pin_motor = pin_motor  # 保存脉冲引脚
        self.pin_direct = pin_direct  # 保存方向引脚
        self.pul = pul  # 保存脉冲数
        self.frequency_list = frequency_list  # 保存频率列表
        self.function = function  # 保存电机功能描述
    
    def StepMotor_Enable(self, pwm_mark):  # 1表示使用PWM，0表示使用GPIO
        """
        启用步进电机，将引脚设置为输出模式
        :param pwm_mark: 1表示使用PWM，0表示使用GPIO
        """
        GPIO.setup(self.pin_motor, GPIO.OUT)  # 设置脉冲引脚为输出模式
        GPIO.setup(self.pin_direct, GPIO.OUT)  # 设置方向引脚为输出模式
        if pwm_mark > 1:
            # 如果pwm_mark大于1，初始化PWM
            self.pwm = GPIO.PWM(self.pin_motor, self.frequency_list[0])  # 默认频率为频率列表中的第一个值
            self.pwm.start(0)  # 启动PWM，初始占空比为0
            self.pwm.ChangeDutyCycle(0)  # 设置占空比为0
    
    def StepMotor_frequency_run(self, direct, frequency_speed_loc):
        """
        以指定频率运行步进电机
        :param direct: 运行方向
        :param frequency_speed_loc: 频率列表中的位置
        """
        GPIO.output(self.pin_direct, direct)  # 设置方向引脚的电平
        self.pwm.ChangeDutyCycle(60)  # 设置占空比为60%
        self.pwm.ChangeFrequency(self.frequency_list[frequency_speed_loc])  # 设置PWM频率为频率列表中的指定值
    
    def StepMotor_frequency_stop(self):
        """
        停止步进电机
        """
        self.pwm.ChangeDutyCycle(0)  # 设置占空比为0，停止电机
    
    def StepMotor_gpio_run(self, direct, gpio_speed, stop_sign):
        """
        以GPIO方式运行步进电机
        :param direct: 运行方向
        :param gpio_speed: GPIO速度
        :param stop_sign: 停止标志
        """
        GPIO.output(self.pin_direct, direct)  # 设置方向引脚的电平
        while stop_sign == True:
            # 当停止标志为True时，循环运行电机
            GPIO.output(self.pin_motor, GPIO.HIGH)  # 设置脉冲引脚为高电平
            time.sleep(gpio_speed)  # 等待指定时间
            GPIO.output(self.pin_motor, GPIO.LOW)  # 设置脉冲引脚为低电平
            time.sleep(gpio_speed)  # 等待指定时间
    
    def StepMotor_gpio_angle(self, direct, angle, gpio_speed):
        """
        以指定角度运行步进电机
        :param direct: 运行方向
        :param angle: 运行角度
        :param gpio_speed: GPIO速度
        """
        GPIO.output(self.pin_direct, direct)  # 设置方向引脚的电平
        loc = (int)((angle / 360) * self.pul)  # 计算需要运行的脉冲数
        for i in range(loc):
            # 循环运行电机，直到达到指定角度
            GPIO.output(self.pin_motor, GPIO.HIGH)  # 设置脉冲引脚为高电平
            time.sleep(gpio_speed)  # 等待指定时间
            GPIO.output(self.pin_motor, GPIO.LOW)  # 设置脉冲引脚为低电平
            time.sleep(gpio_speed)  # 等待指定时间
