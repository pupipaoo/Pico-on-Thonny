import tcs34725
import time
from machine import I2C, Pin
def handler(pin):
    print("interrupt!")
    sensor.interrupt(False)
i2c = I2C(0, sda=Pin(12), scl=Pin(13))
sensor = tcs34725.TCS34725(i2c)
sensor.active(True)
sensor.gain(4)  #1,4,16,60
#sensor.integration_time(402)    
int_pin = Pin(11, Pin.IN, Pin.PULL_UP)
int_pin.irq(handler=handler, trigger=Pin.IRQ_FALLING)
#sensor.threshold(1, 10000, 30000)


time.sleep_ms(500)

while True:
    sensor_data = sensor.read(10)
    print("R = ", sensor_data[0])
    print("G = ", sensor_data[1])
    print("B = ", sensor_data[2])
    print("Brightness = ", sensor_data[3])
    print("===================================")
    sensor.threshold(1, 10000, 30000)
    time.sleep_ms(200)