from time import sleep
sensor_vol=machine.ADC(1)
conversion_factor=3.3/65535
while True:
    vol=sensor_vol.read_u16() * conversion_factor
    vol_a=round(vol/10,2)
    vol_b=round(vol)
    disp=str(vol_a)
    print(disp)
    sleep(0.2)