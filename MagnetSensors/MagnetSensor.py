import RPi.GPIO as GPIO

class MagnetSensor:
    def __init__(self,pin_sensor,function):
        self.pin_sensor = pin_sensor
        self.function = function

    def MagnetSensor_Enable(self):
        GPIO.setup(self.pin_sensor,GPIO.IN,pull_up_down=GPIO.PUD_UP) #默认上拉

    def MagnetSensor_detect(self):
        pin_data = GPIO.input(self.pin_sensor)
        return pin_data