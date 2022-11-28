from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine

print(os.uname())

sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
lens = len('GET /update?api_key=ORAIVXS2FDL752J7&field1="+temp+"\r\n')      #GET method傳送過去的資料量的長度
Len = str(lens)         #轉成字串
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

sendCMD_waitResp('AT+CWJAP="My ASUS","jade1234"\r\n', 5000) #connecting #5000是PORT

sendCMD_waitResp("AT+CIPMUX=0\r\n")  # multi user

print("RPi-PICO with ESP-01")
while True:
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.00721, 1)
    print(temp)
    temp=str(temp)
    sendCMD_waitResp('AT+CIPSTART="TCP","184.106.153.149",80\r\n',500)
    sendCMD_waitResp("AT+CIPSEND="+Len+"\r\n",500)      #是指送幾個BYTE,也就是板子透過TCP送多少資料量給THINGSPEAK，500ms是指等多少時間
    sendCMD_waitResp("GET /update?api_key=ORAIVXS2FDL752J7&field1="+temp+"\r\n")    #GET 路徑?key=value&key=value \r\n    #temp原本就自串
    sendCMD_waitResp("AT+CIPCLOSE\r\n")         #TCP斷線，因為連線到https，很消耗記憶體
    utime.sleep(5)

sendCMD_waitResp("AT+CIPCLOSE=0\r\n")
