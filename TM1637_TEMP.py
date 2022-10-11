import sys,os
import onewire
import tm1637
from machine import Pin, PWM, I2C, UART, ADC
from utime import sleep

tm = tm1637.TM1637(clk=Pin(13), dio=Pin(12))  #設定tm1637 Pin
sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
# all LEDS off
tm.write([0, 0, 0, 0])
tm.show('    ')
while(True):
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.001721) 
    print(temp)
#    tm.scroll('Hello')
#    tm.brightness(7)
    tm.number(temp) 
    sleep(1)
    

    