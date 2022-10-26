 # 2, simple application of TCS34725:
# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com
# https://techtotinker.blogspot.com/2021/04/033-micropython-technotes-tcs34725-rgb.html
from machine import Pin
from machine import I2C
from machine import PWM
from time import sleep_ms
from tcs34725 import TCS34725
#from gorillacell_rgb import GORILLACELL_RGB

sensor = I2C(0, sda=Pin(12), scl=Pin(13))
tcs = TCS34725(sensor)
#rgb = GORILLACELL_RGB(25, 26, 27)

while True:
    print(tcs.read('dec'))
    print(tcs.read('raw'))
    
    #red, grn, blu = tcs.read('dec')
    #rgb.set_rgb(red, grn, blu)第四個數字是亮度