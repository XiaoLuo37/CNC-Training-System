import RPi.GPIO as GPIO

class RedSensor:
    def __init__(self,pin,function):
        self.pin = pin
        self.function = function
        
    def RedSensor_Enable(self):
        GPIO.setup(self.pin,GPIO.IN)
    
    def RedSensor_detect(self):
        state = GPIO.input(self.pin)
        return state