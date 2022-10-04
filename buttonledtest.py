import machine
from time import sleep
button=machine.Pin(11,machine.Pin.IN,machine.Pin.PULL_UP)
pin_led=machine.Pin(25,machine.Pin.OUT)
x=1
    if button.value()==0:
        x+=x
        for i in range(x):
            pin_led.on()
    else:
        pin_led.off()