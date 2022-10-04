from machine import Pin,PWM
from time import sleep
pwm=PWM(Pin(28))
pin_bee=machine.Pin(28,machine.Pin.OUT)

while True:
    pwm.duty_u16(10000)
    pwm.freq(3000)
    sleep(1)
