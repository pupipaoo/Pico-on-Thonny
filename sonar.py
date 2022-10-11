import time
from machine import Pin
import hc_sr04
trig=Pin(10,Pin.OUT)
echo = Pin(4,Pin.IN)
def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=()
    timeout=False
    start=time.ticks_us()
    while not echo.value():
        time.sleep_us(10)
        count+=1
        if count>100000:
            timeout=True
            break
        if timeout:
            duration=0
        else:
            count=0
            start=time.ticks_us()
    while echo.value():
        time.sleep_us(10)
        count+=1
        if count>2320:
            break
        duration=time.ticks_diff(time.ticks_us(),start)
    return duration
    
while True:
        distance=round(ping9()/58)
        print('%scm'%distance)
        time.sleep(0.5)