from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine
from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
import utime as time
from dht import DHT11, InvalidChecksum

print(os.uname())
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper())   # Display device address
print("I2C Configuration: "+str(i2c))                     # Display I2C config
 
pin = Pin(28, Pin.OUT, Pin.PULL_UP) 
oled = SSD1306_I2C(128, 32, i2c)                 # Init oled display
sensor = DHT11(pin)

sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
lens = len('GET /update?api_key=ORAIVXS2FDL752J7&field1="+temp+"&field2="+humi+"\r\n')
Len = str(lens)
print(lens)
utime.sleep(1)
#functions
def sendCMD_waitResp(cmd, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd.encode('utf-8'))
    waitResp(timeout)
    print()
    
def waitResp(timeout=20000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills) < timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print(resp)
    
#print uart info
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
print(uart)
#waitResp() 
sendCMD_waitResp("AT+RST\r\n") #reset the esp8266

sendCMD_waitResp("AT+CWMODE=1\r\n")   #set wifi mode 1:client 2:AP 3: Both

sendCMD_waitResp('AT+CWJAP="My ASUS","jade1234"\r\n', 5000) #connecting

sendCMD_waitResp("AT+CIPMUX=0\r\n")  # multi user

print("RPi-PICO with ESP-01")

while True:
    time.sleep(1)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(t))  
    print("Humidity: {}".format(h))
    # Clear the oled display in case it has junk on it.       
    
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.00721, 1)
    print(temp)
    temp=str(temp)#上船數值要用字串
    humi=str(h)#上傳數值要用字串
    sendCMD_waitResp('AT+CIPSTART="TCP","184.106.153.149",80\r\n',500)
    sendCMD_waitResp("AT+CIPSEND="+Len+"\r\n",500)
    sendCMD_waitResp("GET /update?api_key=ORAIVXS2FDL752J7&field1="+temp+"&field2="+humi+"\r\n")
    sendCMD_waitResp("AT+CIPCLOSE\r\n")
    utime.sleep(5)

sendCMD_waitResp("AT+CIPCLOSE=0\r\n")