# # 定时器初始化。period:單位 ms（毫秒）
# mode：2 種工作模式，Timer.ONE_SHOT（執行一次）、Timer.PERIODIC（周期性）
#callback:定时器中断後的函数。
from machine import Pin, Timer
import time

led = Pin(25, Pin.OUT)
led14 = Pin(14,Pin.OUT)
led15 = Pin(15,Pin.OUT)
tim1 = Timer()
tim2 = Timer()

def tick(timer):
    led14.toggle()
  
def label1(timer):
    led15.toggle()

tim1.init(freq=20, mode=Timer.PERIODIC, callback=tick)
tim2.init(freq=1, mode=Timer.ONE_SHOT, callback=label1)

while True :
    time.sleep (1)
    led.toggle()
