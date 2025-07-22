import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self,function,StepMotor_list,RedSensor_list,PushRod_list):
        self.function = function
        self.StepMotor_list = StepMotor_list
        self.RedSensor_list = RedSensor_list
        self.PushRod_list = PushRod_list

    def RedSensor_to_reset(self):
        pin_direct = GPIO.HIGH #LOW往右
        speed_loc = 1

        while self.RedSensor_list[1].RedSensor_detect() == GPIO.HIGH and self.RedSensor_list[3].RedSensor_detect() == GPIO.HIGH:
            self.StepMotor_list[1].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc) #'z'
            self.StepMotor_list[2].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc) #'d'
        print('reset round1 over')

        speed_loc = 1

        if self.RedSensor_list[1].RedSensor_detect() == GPIO.HIGH:
            while self.RedSensor_list[1].RedSensor_detect() == GPIO.HIGH:
                self.StepMotor_list[1].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('reset z')
        else:
            current_time = time.time()
            while abs(time.time() - current_time) <= 1:
                self.StepMotor_list[1].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('reset z')
        
        self.StepMotor_list[1].StepMotor_frequency_stop()
        if self.RedSensor_list[3].RedSensor_detect() == GPIO.HIGH:
            while self.RedSensor_list[3].RedSensor_detect() == GPIO.HIGH:
                self.StepMotor_list[2].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('reset d')
        else:
            current_time = time.time()
            while abs(time.time() - current_time) <= 1:
                self.StepMotor_list[2].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('reset d')
        self.StepMotor_list[2].StepMotor_frequency_stop()
        print('reset round2 over')

    def RedSensor_to_start(self):
        pin_direct = GPIO.LOW #HIGH往左
        speed_loc = 1
        while self.RedSensor_list[0].RedSensor_detect() == GPIO.HIGH and self.RedSensor_list[2].RedSensor_detect() == GPIO.HIGH:
            self.StepMotor_list[1].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            self.StepMotor_list[2].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
        print('start round1 over')

        speed_loc = 1

        if self.RedSensor_list[0].RedSensor_detect() == GPIO.HIGH:
            while self.RedSensor_list[0].RedSensor_detect() == GPIO.HIGH:
                self.StepMotor_list[1].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('start z')
        else:
            print('start z')
        self.StepMotor_list[1].StepMotor_frequency_stop()

        if self.RedSensor_list[2].RedSensor_detect() == GPIO.HIGH:
            while self.RedSensor_list[2].RedSensor_detect() == GPIO.HIGH:
                self.StepMotor_list[2].StepMotor_frequency_run(direct=pin_direct,frequency_speed_loc=speed_loc)
            print('start d')
        else:
            print('start d')
        self.StepMotor_list[2].StepMotor_frequency_stop()
        print('start round2 over')

    def PushRod_push(self):
        self.PushRod_list[0].PushRod_run(0)
        time.sleep(1.5)
    
    def PushRod_pull(self):
        self.PushRod_list[0].PushRod_run(1)
        time.sleep(1.5)