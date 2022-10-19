'''TCP  利用手機透過WIFI控制LED燈'''

from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine
from time import sleep

print(os.uname())

led = machine.Pin(25, machine.Pin.OUT)
led.value(0)
utime.sleep(0.5)
led.value(1)
utime.sleep(0.5)
led.value(0)

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
'''
def waitRespLine(timeout = 2000):
    prvMills = utime.ticks_ms()
    while (utime.ticks_ms() - prvMills) < timeout:
        if uart.any():
            print(uart.readline().dencode('utf-8'))
'''            
#print uart info
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
print(uart)

#waitResp() 
sendCMD_waitResp("AT+RST\r\n") #reset the esp8266
#AT command test
sendCMD_waitResp("AT\n\r")
sendCMD_waitResp("AT+GMR\r\n") #firmware version

utime.sleep(0.5)
sendCMD_waitResp("AT+RST\r\n") #reset the esp8266
sendCMD_waitResp("AT+CWMODE?\r\n") #chekck wifi mode
sendCMD_waitResp("AT+CWMODE=3\r\n") #set wifi mode 1:client 2:AP 3: Both
sendCMD_waitResp("AT+CWLAP\r\n", 5000) #all list of AP

utime.sleep(0.5)  #add
sendCMD_waitResp('AT+CWJAP="My ASUS","jade1234"\r\n', 10000) #connecting

utime.sleep(0.5)
sendCMD_waitResp("AT\r\n")
sendCMD_waitResp("AT+CIPSTATUS\r\n")

#UDP SERVER
sendCMD_waitResp("AT+CIPMUX=1\r\n") #TCP/UDP Connections - multiple
sendCMD_waitResp("AT+CIPSERVER=1,80\r\n")
sendCMD_waitResp('AT+CIPSTART=0,"UDP","0.0.0.0",4321,4320,2\r\n')

sendCMD_waitResp("AT+CIFSR\r\n", 5000) #check status and ip address
print("connected...")
print("RPi-PICO with esp8266")
while True:
    if uart.any()> 0:
        sleep(0.1)
        respon = uart.readline()
        print(respon)
        resp=str(respon)
        if (resp.find("on"))>=0:
            led.value(1)
            print(resp[12:16])
            utime.sleep(0.5)
            sendCMD_waitResp('AT+CIPSEND=1,6\r\n')
            sendCMD_waitResp("LED ON")
        elif (resp.find("off"))>=0:
            led.value(0)
            print(resp[12:17])
            utime.sleep(0.5)
            sendCMD_waitResp("AT+CIPSEND=1,7\r\n")
            sendCMD_waitResp("LED OFF")
        
        
sendCMD_waitResp("AT+CIPCLOSE=0\r\n")