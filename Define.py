import RPi.GPIO as GPIO

port = 8022

PUL = 400

recv_len = 4
recv_from_qt = ''

frequency_list = [900,1200,1400]

#暂时由M8复用而来
detect_nfc = 9

gcode = """N10 G21
N20 G17
N30 G90
N40 G0 Z5
N50 G0 X0 Y0
N60 G0 X50 Y50
N70 G1 Z1 F100
N80 G1 X100
N90 G1 Y100
N100 G1 X150
N110 G1 Y150
N120 G0 Z5
N130 G0 X0 Y0
N140 G1 Z1 F100
N150 G1 X50 Y50
N160 G0 Z5
M3
N170 G0 X100 Y100
N180 G1 Z1 F100
N190 G1 X150 Y150
N200 G1 X200 Y200
N210 G0 Z5
N220 G0 X0 Y0
N230 G1 Z1 F100
N240 G1 X50 Y50
N250 G0 Z5
M5
N260 G0 X100 Y100
N270 G1 Z1 F100
N280 G1 X150 Y150
N290 G1 X200 Y200
N300 G0 Z5
N310 G0 X0 Y0
N320 G1 Z1 F100
N330 G1 X50 Y50
N340 G0 Z5
"""

StepMotor_list=[]
PushRod_list=[]
RedSensor_list=[]
PressSensor_list=[]
MagnetSensor_list=[]
Control_list=[]
Serial_list=[]

# Serial_dict={
#     'TXD': 14,
#     'RXD': 15
# }

StepMotor_dict = {  #[PUL,DIR]
    'x':[0,5],
    'z':[13,26],
    'd':[21,20],  #前三种都是PWM控制

    'y':[16,12]   #GPIO控制
 }

PushRod_dict = {
    'L':[24,25]
}

RedSensor_dict ={
    'r1': 14,     #'z'轴左
    'r2': 15,     #'z'轴右
    'r3': 18,    #'d'轴左
    'r4': 23     #'d'轴右
}

PressSensor_dict = {
    'R1':8,
    'R2':7
}

MagnetSensor_dict = {
    'M1':2,
    'M2':3,
    'M3':4,
    'M4':17,
    'M5':27,
    'M6':22,
    'M7':10,
    'M8':9,        #暂时复用为检测按钮
    'M9':11
}

commands = { #'电机 方向 档速 动/停'
    '0000':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=0), #'x'轴 逆时针 三档速
    '0001':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '0010':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=1),
    '0011':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '0020':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=2),
    '0021':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '0100':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=0), #'x'轴 顺时针 三档速
    '0101':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '0110':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=1),
    '0111':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '0120':lambda:StepMotor_list[0].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=2),
    '0121':lambda:StepMotor_list[0].StepMotor_frequency_stop(),
    '1000':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=0), #'z'轴 逆时针 三档速
    '1001':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '1010':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=1),
    '1011':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '1020':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=2),
    '1021':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '1100':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=0), #'z'轴 顺时针 三档速
    '1101':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '1110':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=1),
    '1111':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '1120':lambda:StepMotor_list[1].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=2),
    '1121':lambda:StepMotor_list[1].StepMotor_frequency_stop(),
    '2000':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=0), #'d'轴 逆时针 三档速
    '2001':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '2010':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=1),
    '2011':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '2020':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.LOW,frequency_speed_loc=2),
    '2021':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '2100':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=0), #'d'轴 顺时针 三档速
    '2101':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '2110':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=1),
    '2111':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '2120':lambda:StepMotor_list[2].StepMotor_frequency_run(direct=GPIO.HIGH,frequency_speed_loc=2),
    '2121':lambda:StepMotor_list[2].StepMotor_frequency_stop(),
    '3000':lambda:None,
    '3001':lambda:StepMotor_list[3].StepMotor_gpio_angle(0,45,0.001),
    '3100':lambda:None,
    '3101':lambda:StepMotor_list[3].StepMotor_gpio_angle(1,45,0.001),
    'star':lambda:Control_list[0].RedSensor_to_start(),
    'rese':lambda:Control_list[0].RedSensor_to_reset(),
    'pull':lambda:Control_list[0].PushRod_pull(),
    'push':lambda:Control_list[0].PushRod_push(),
    'rol0':lambda:StepMotor_list[3].StepMotor_gpio_angle(0,45,0.001),
    'rol1':lambda:StepMotor_list[3].StepMotor_gpio_angle(1,45,0.001),
    'inpu':lambda:None,
}

#    3V3  (1) (2)  5V    
#  GPIO2  (3) (4)  5V    
#  GPIO3  (5) (6)  GND   
#  GPIO4  (7) (8)  GPIO14
#    GND  (9) (10) GPIO15
# GPIO17 (11) (12) GPIO18
# GPIO27 (13) (14) GND   
# GPIO22 (15) (16) GPIO23
#    3V3 (17) (18) GPIO24
# GPIO10 (19) (20) GND   
#  GPIO9 (21) (22) GPIO25
# GPIO11 (23) (24) GPIO8
#    GND (25) (26) GPIO7 
#  GPIO0 (27) (28) GPIO1 
#  GPIO5 (29) (30) GND   
#  GPIO6 (31) (32) GPIO12
# GPIO13 (33) (34) GND   
# GPIO19 (35) (36) GPIO16
# GPIO26 (37) (38) GPIO20
#    GND (39) (40) GPIO21
