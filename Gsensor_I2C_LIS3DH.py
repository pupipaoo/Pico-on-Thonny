from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
#import time, uos, utime
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=100000)
print('Gsensor LIS3DH...')

i2c.start
i2c.writeto(0x19, bytes([0x20,0x47]))   #41:x / 42:y / 44:z / 47:x,y,z
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x21,0x80]))   #0x80/0x88
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x22,0x00]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x23,0x00]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x24,0x40]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x25,0x00]))
i2c.stop

while True:
    i2c.start
    i2c.writeto(0x19, bytes([0xa8])) 
    data = i2c.readfrom(0x19,6)
    i2c.stop
    x = round((((data[0])>>6 | (data[1])<<2)))
    y = round((((data[2])>>6 | (data[3])<<2)))
    z = round((((data[4])>>6 | (data[5])<<2)))
    print('{}{:4}{}{:4}{}{:4}'.format('X =',x,'  Y =',y ,'  Z =',z))
    sleep(0.5)

    
  