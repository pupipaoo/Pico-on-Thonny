#將溫度值顯示於OLED上

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
from time import sleep
import math

sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=200000)
oled = SSD1306_I2C(128, 32, i2c)

while True:
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.001721, 2)
    print(temp)
    sleep(1)    
    disp=str(temp)
    oled.fill(0)
    oled.text(disp,80,10)
    oled.show()
    
    
