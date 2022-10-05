from machine import Pin
from time import sleep
pin_led0=machine.Pin(14,machine.Pin.OUT)
pin_led1=machine.Pin(15,machine.Pin.OUT)
pin_led2=machine.Pin(25,machine.Pin.OUT)
button=machine.Pin(11,machine.Pin.IN,machine.Pin.PULL_UP)
sw_time=0.5
i=0
LEDS=['pin_led0','pin_led1','pin_led2']
LEDS2=['pin_led2','pin_led1','pin_led0']
while True:
    if button.value()==0:
        for k in range(0,3):
            s=eval(LEDS[k%3])
            s.toggle()
            sleep(sw_time)
    else:
        for k in range(0,3):
            s=eval(LEDS2[k%3])
            s.toggle()
            sleep(sw_time)