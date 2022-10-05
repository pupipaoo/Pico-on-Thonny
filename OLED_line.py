from machine import Pin, I2C
import utime
from ssd1306  import SSD1306_I2C

sda=machine.Pin(12)
scl=machine.Pin(13)
width=128
height=32
i2c = I2C(0, scl=scl, sda=sda, freq=400000)
oled = SSD1306_I2C(width, height, i2c)                  # Init oled display

oled.fill(0)

oled.hline(1,2,100,1)   #在(1,2)畫一長100的水平線
oled.vline(1,2,20, 1)   #在(1,2)畫一高10的垂直線
oled.text("Hello!!", 10, 8, 1)   #在(10,8)顯示 Hello world!    
oled.line(1, 22, 100, 22, 1)  # 在(1, 50)和(100, 60)兩點畫一條
oled.vline(100,2,20, 1)   #在(100,2)畫一高10的垂直線
oled.show()    #顯示上面的圖形