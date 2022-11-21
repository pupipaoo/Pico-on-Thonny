from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine
import random
#from ssd1306 import SSD1306_I2C

print(os.uname())

WiFi_SSID='iloveiot'
WiFi_PASSWD=''
Sever_IP='125.229.69.35'
Sever_port=3001

print("RPi-PICO with ESP-01")
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
#oled = SSD1306_I2C(128, 32, i2c)
#oled.fill(0)

led = machine.Pin(25, machine.Pin.OUT)
led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)
led1.value(0)
led2.value(0)
led.value(0)


#functions


def sendCMD_waitResp(cmd,timeout=100):
    
    print("CMD: " + cmd)
    cmd+='\r\n'
    uart.write(cmd)  #cmd.encode('utf-8')
    return waitResp(timeout)
   
    
def waitResp(timeout=2000,debug=False):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills) < timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    
    if debug:
        print(str(resp))
    
    return str(resp)

    
      
#print uart info
def connet_wifi(ssid, passwd):
    
    #waitResp() 
    sendCMD_waitResp("AT+RST") #reset the esp8266       #sendCMD是ESP8266的AT Command
    sendCMD_waitResp("AT+CWMODE=0")   #set wifi mode 1:client 2:AP 3: Both  #開啟wifi 模式
    sendCMD_waitResp('AT+CWJAP='+"My ASUS"+','+"jade1234",timeout=5000) #connecting
    sendCMD_waitResp("AT+CIPMUX=0")  # 0: single connection(自己去連別人); 1:multi user(多人連線，連很多serever,被別人連才用這個)
    resp=sendCMD_waitResp("AT+CIFSR")
    start=resp.find('"')+1
    end=resp.find('"',start)
    return resp[start:end]  #myip
    
  
    
    
def send_http_req(ip,port,url,method='GET'):            #HTTP訊息以get送出

    #GET /sensor?temp=28 HTTP/1.1\r\n\r\n'
    url=method+' '+url+' HTTP/1.1\r\n\r\n'
    sendCMD_waitResp('AT+CIPSTART="TCP","'+ip+'",'+str(port))
    sendCMD_waitResp('AT+CIPSEND='+str(len(url)))       #算送了幾個byte,並送出
    sendCMD_waitResp(url)               #送url
    sendCMD_waitResp("AT+CIPCLOSE")


myip=connet_wifi(WiFi_SSID,WiFi_PASSWD)
#oled.fill(0)
#oled.text(myip,0,0)
#oled.show()
utime.sleep(5)

while (1):
    i=round(random.uniform(30,60),2)    #i是隨便的數字
    url_path='/sensor?temp='+str(i)
    #oled.fill(0)
    #oled.text('temp='+str(i),0,0)
    #oled.show()
    send_http_req(Sever_IP,Sever_port,url_path)
 

     

