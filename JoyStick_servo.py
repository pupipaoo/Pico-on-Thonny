import machine
import time
from machine import Pin, PWM, Timer

x=machine.ADC(26)
y=machine.ADC(28)
servo_x = PWM(Pin(16))
servo_y = PWM(Pin(17))
servo_x.freq(50)
servo_y.freq(50)

x_zero = x.read_u16()/400
y_zero = y.read_u16()/400

Duty = 0
def servo(degrees):
    global Duty
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0   
    maxDuty=8000
    minDuty=2000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    Duty = newDuty
    return Duty

    
while True:
    reading=x.read_u16()
    x_data = round(x_zero-reading/400)
    print('X= ',x_data)
    reading=y.read_u16()
    y_data = round(y_zero-reading/400)
    #print('X= ',x_data)
    y_data+=90
    print('YD= ',y_data)
    if y_data<=0 :
        y_data=-y_data
        print('-Y= ',y_data)
        servo(y_data)
        servo_y.duty_u16(int(Duty))
    else :
        print('Y= ',y_data)
        servo(y_data)
        servo_y.duty_u16(int(Duty))
    time.sleep(0.1)
