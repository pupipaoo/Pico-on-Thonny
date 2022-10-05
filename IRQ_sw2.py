from machine import Pin
from time import sleep

led_14 = Pin(14, Pin.OUT)
led_15 = Pin(15, Pin.OUT)
led_25 = Pin(25, Pin.OUT)

led_14.value(0)
led_15.value(0)
led_25.value(0)

button_11 = Pin(11, Pin.IN, Pin.PULL_UP)
x=0
y=0
def int_handler(pin):
    global x
    global y
    button_11.irq(handler=None)    # disable irq
    print("Interrupt Detected!")
    y=1
    x+=1
    if x >= 3:
        x=0
    while button_11.value() == 0:
        sleep(0.1)
    button_11.irq(handler=int_handler)  #enable irq
    
def Delay(T):
    global y
    for i in range (T):
        sleep(0.01)
        if y==1 :
            break
button_11.irq(trigger=Pin.IRQ_FALLING, handler=int_handler)  #IRQ_FALLING/RISING

while True:
    if x == 0:
        led_15.toggle()
        Delay(200)
        print(y)
        led_14.toggle()
        Delay(200)
        print(y)
        led_25.toggle()
        Delay(200)
        print(y)
        y=0
    elif x== 1:
        led_25.toggle()
        Delay(200)
        led_14.toggle()
        Delay(200)
        led_15.toggle()
        Delay(200)
        y=0
    else :
        led_15.value(0)
        led_14.value(0)
        led_25.value(0)

        
     