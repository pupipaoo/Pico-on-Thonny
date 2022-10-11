
import machine
import utime

uart0 = machine.UART(0,baudrate=115200)  #at-command

def sendCMD_waitResp(cmd, uart=uart0, timeout=100):
    print("CMD: " + cmd)
    uart.write(cmd)


    
def waitResp(uart=uart0, timeout=100):
    global data
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
            print(resp)

print(uart0)
print("- uart0 -")
sendCMD_waitResp("start\r\n")

while True :
    waitResp()
    sendCMD_waitResp('123\r\n')
    utime.sleep(1)
