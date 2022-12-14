from machine import Pin,Timer    #Timer是計時器套件
import time

led=Pin(25,Pin.OUT)
led14=Pin(14,Pin.OUT)
led15=Pin(15,Pin.OUT)
tim1=Timer()     #建立執行緒1
tim2=Timer()     #建立執行緒2

def tick(timer):
    led14.toggle()
def labell(timer):
    led15.toggle()

tim1.init(freq=20,mode=Timer.PERIODIC,callback=tick)  #init公式類似執行緒1，透過設定時間製造中斷點,可以在while迴圈運作時，同時跑回執行這段程式，並且每隔0.05秒再進行一次
tim2.init(freq=1,mode=Timer.ONE_SHOT,callback=labell)                                     
while True:
    time.sleep(1)
    led.toggle()



