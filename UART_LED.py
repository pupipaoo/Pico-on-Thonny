import uos
import machine
import utime
data = b"" #這是databit的社訂嗎? databit:通常設定8bit,這樣才知道每傳過去8位元即成一個字元
print(uos.uname())
uart0 = machine.UART(0,baudrate=115200)  #at-command #baurate=每秒傳幾bit

def sendCMD_waitResp(cmd, uart=uart0, timeout=1000):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()
    
def waitResp(uart=uart0, timeout=500):
    global data
    prvMills = utime.ticks_ms()
    #resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            data = b"".join([data, uart.read(1)])           

#indicate program started visually
led_onboard = machine.Pin(25, machine.Pin.OUT)
print(uart0)
print("- uart0 -")
sendCMD_waitResp("start\r\n")

while True :
    waitResp()
    if data != b"" :
        print(data)
        if data == b'on':
            led_onboard.value(1)
            sendCMD_waitResp('LED_ON\r\n')
        elif data == b'off':
            led_onboard.value(0)
            sendCMD_waitResp('LED_OFF\r\n')
        data = b""
    utime.sleep(0.1)
