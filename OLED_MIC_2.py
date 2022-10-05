from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import machine

sensor_vol=machine.ADC(1)
sensor_ext=machine.ADC(2)
conversion_factor = 3.3 / 65535
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=200000)
oled = SSD1306_I2C(128, 32, i2c)
pin_led1 = machine.Pin(14, machine.Pin.OUT)
pin_led2 = machine.Pin(15, machine.Pin.OUT)
pin_led  = machine.Pin(25, machine.Pin.OUT)
x=0
m="o"

while True:
    vol=sensor_vol.read_u16() * conversion_factor
    vol_a= round(vol,2)
    vol_b= round(vol*10)
    if vol_b>19 or vol_b<14:
        pin_led1.on()
    else:
        pin_led1.off()
    if vol_b>22 or vol_b<10:
        pin_led2.on()
    else:
        pin_led2.off()
    if vol_b>26 or vol_b<7:
        pin_led.on()
    else:
        pin_led.off()
    disp=str(vol_b)
    print(disp)
    oled.text(m,x,vol_b)
    x=x+1
    if x==127:
        x=0
    oled.text(disp,50,0)
    oled.show()
    sleep(0.05)
    oled.fill(0)
