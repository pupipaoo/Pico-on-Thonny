from machine import Pin,PWM
from time import sleep
pwm=PWM(Pin(25))
pwm.freq(50)
while True:
    for i in range(1000,20000,1):
        pwm.duty_u16(i)
        sleep(0.0001)
    sleep(0.3)
    for i in range(20000,1000,-1):
        pwm.duty_u16(i)
        sleep(0.0001)
    sleep(0.3)