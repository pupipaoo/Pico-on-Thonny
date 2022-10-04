from machine import PWM, Pin
from time import sleep
littlestar = ["C3", "C3", "G3", "G3", "A3", "A3", "G3", "0", "F3", "F3",
                  "E3", "E3", "D3", "D3", "C3", "0", "G3", "G3", "F3", "F3",
                  "E3", "E3", "D3", "0", "G3", "G3", "F3", "F3",
                  "E3", "E3", "D3", "0","C3", "C3", "G3", "G3", "A3", "A3", "G3", "0", "F3", "F3",
                  "E3", "E3", "D3", "D3", "C3", "0"]
speaker = PWM(Pin(28))
led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
def playnote(Note, Duration):
    if Note == "0":
        sleep(Duration)
    if Note == "S":
        speaker.duty_u16(0)
        sleep(Duration)
    elif Note != "0":
        speaker.duty_u16(0)
        sleep(0.05)
        led1.toggle()
        led2.toggle()
        speaker.duty_u16(3000)        
        speaker.freq(MusicNotes[Note])
        print (MusicNotes[Note])
        sleep(Duration)
led1.on()
led2.off()
for c in littlestar:
    playnote(c, 0.2)

speaker.duty_u16(0)
