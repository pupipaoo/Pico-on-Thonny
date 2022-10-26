from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
import utime as time
from dht import DHT11, InvalidChecksum
#import DHT11 
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper())   # Display device address
print("I2C Configuration: "+str(i2c))                     # Display I2C config
 
pin = Pin(28, Pin.OUT, Pin.PULL_UP) 
oled = SSD1306_I2C(128, 32, i2c)                 # Init oled display
sensor = DHT11(pin)

while True:
    time.sleep(1)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(t))  
    print("Humidity: {}".format(h))
    # Clear the oled display in case it has junk on it.
    oled.fill(0)       

    oled.text("Temp: ",10,5)
    oled.text(str(sensor.temperature),60,5)
    oled.text("*C",100,5)
    
    oled.text("Humi: ",10,20)
    oled.text(str(sensor.humidity),60,20)
    oled.text("%",100,20)
    time.sleep(1)
    oled.show()