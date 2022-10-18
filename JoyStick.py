import machine
import time

x=machine.ADC(26)
y=machine.ADC(28)

time.sleep(0.5)
x_zero = x.read_u16()/100
y_zero = y.read_u16()/100
while True:
    reading=x.read_u16()
    x_data = round(x_zero-reading/100)
    print('X= ',x_data)
    reading=y.read_u16()
    y_data = round(y_zero-reading/100)
    print('Y= ',y_data)
    time.sleep(0.5)
    