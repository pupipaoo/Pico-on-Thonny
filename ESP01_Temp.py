from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine

print(os.uname())

sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
link = machine.Pin(25, machine.Pin.OUT)
led = machine.Pin(15, machine.Pin.OUT)
led.value(0)
link.value(0)

#functions
def sendCMD_waitResp(cmd, timeout=1000):
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
sendCMD_waitResp("AT+CWMODE?\r\n") #chekck wifi mode
sendCMD_waitResp("AT+CWMODE=3\r\n") #set wifi mode 1:client 2:AP 3: Both
sendCMD_waitResp("AT+CWLAP\r\n", 5000) #all list of AP
sendCMD_waitResp('AT+CWJAP="My ASUS","jade1234"\r\n', 10000) #connecting  Walter_4G #10000是PORT
sendCMD_waitResp("AT\r\n")
sendCMD_waitResp("AT+CIPSTATUS\r\n")
sendCMD_waitResp("AT+CIPMUX=1\r\n") #TCP/UDP Connections - multiple
sendCMD_waitResp("AT+CIPSERVER=1,80\r\n")
sendCMD_waitResp("AT+CIFSR\r\n", 5000) #check status and ip address
utime.sleep(1)
print("RPi-PICO with esp8266")
while True:
    
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.00721, 1)
    print(temp)
    tem=str(temp)
    x=len(tem)
    utime.sleep(0.5)
    sendCMD_waitResp('AT+CIPSEND=0,4\r\n')
    sendCMD_waitResp(tem)
    sendCMD_waitResp('AT+CIPSEND=1,4\r\n')
    sendCMD_waitResp(tem)

sendCMD_waitResp("AT+CIPCLOSE=0\r\n")
