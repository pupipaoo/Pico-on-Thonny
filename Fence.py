import time,math
from machine import Pin, PWM
from time import sleep

pin_led = Pin(25, Pin.OUT)
trig = Pin(10, Pin.OUT)
echo = Pin(4, Pin.IN,Pin.PULL_DOWN)
buzzer = Pin(17, Pin.OUT)
servoPin = PWM(Pin(16))
servoPin.freq(50)

def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=0
    timeout=False
    start=time.ticks_us()
    while echo.value() == 0: #wait for HIGH
        start=time.ticks_us()
    while echo.value() : #wait for HIGH
        stop=time.ticks_us()
    duration = stop - start
    dist = ( duration *0.034) /2
    return dist  
def bi():
    for i in range (3000):
        buzzer.value(1)
        time.sleep_us(150)
        buzzer.value(0)
        time.sleep_us(150)
      
def servo(degrees):
    servoPin.freq(50)
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0   
    maxDuty=8000
    minDuty=1800
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
    
while True:
    distance = round(ping())
    print("%s cm" %distance)
    if distance >= 30 :
        servo(120)
        pin_led.value(0)
    else :
        pin_led.value(1)
        servo(20)
        bi()
        time.sleep(1)
        
