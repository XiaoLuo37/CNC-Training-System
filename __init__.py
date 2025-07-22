import RPi.GPIO as GPIO
import sys
import time
from PyQt5.QtWidgets import *

import My_interface

from Controlls.Control import *
from Define import *
from Servers import Server
from Peripherals.Peripheral import *
from Controlls import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    MyPeripheral = Peripheral()