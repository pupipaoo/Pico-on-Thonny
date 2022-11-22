from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine

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