import machine
from time import sleep
pin_led = machine.Pin(15,machine.Pin.OUT)
pin_led2=machine.Pin(25,machine.Pin.OUT)
pin_led3=machine.Pin(14,machine.Pin.OUT)
count=0
while count<10:
    pin_led.on()
    sleep(1)
    pin_led.off()
    pin_led2.on()
    sleep(1)
    pin_led2.off()
    pin_led3.on()
    sleep(1)
    pin_led3.off()
    count+=1
