import RPi.GPIO as GPIO

class PushRod:
    def __init__(self,pin_l,pin_r,function):
        self.pin_l = pin_l
        self.pin_r = pin_r
        self.function = function

    def PushRod_Enable(self):
        GPIO.setup(self.pin_l,GPIO.OUT)
        GPIO.setup(self.pin_r,GPIO.OUT)
    
    def PushRod_run(self,pin_direct):
        if pin_direct == GPIO.HIGH:
            GPIO.output(self.pin_l,GPIO.HIGH)
            GPIO.output(self.pin_r,GPIO.LOW)
        else:
            GPIO.output(self.pin_l,GPIO.LOW)
            GPIO.output(self.pin_r,GPIO.HIGH)
    
    def PushRod_stop(self):
        GPIO.output(self.pin_l,GPIO.LOW)
        GPIO.output(self.pin_r,GPIO.LOW)