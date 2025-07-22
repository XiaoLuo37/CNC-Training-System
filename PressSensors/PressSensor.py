import RPi.GPIO as GPIO

class PressSensor:
    def __init__(self,pin_sensor,function):
        self.pin_sensor = pin_sensor
        self.function = function
    
    def PressSensor_Enable(self):
        GPIO.setup(self.pin_sensor,GPIO.IN)

    def PressSensor_detect(self):
        pin_data = GPIO.input(self.pin_sensor)
        return pin_data