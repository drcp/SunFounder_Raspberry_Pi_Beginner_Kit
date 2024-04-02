# didn't work smoothly, LED would blink unlike toggleLED.py
import RPi.GPIO as GPIO
from time import sleep
delay = 1
inPin=40
outPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pressed=0
pressed_old=1
led=0   #using pull_up resistor, led is off b/c PUD is not seeing ground

def btn_switch(outPin, led_onoff): # turns led off if on and the opposite
    if led_onoff == 1:
        led_onoff = GPIO.output(outPin,0)
        return led_onoff
    else :
        led_onoff = GPIO.output(outPin,1)
        return led_onoff
try:
    while True:
        pressed=GPIO.input(inPin)
        print(pressed)
        #if pressed == 1:
            # button is not pressed nothing happens, pressed == 0
        if pressed==0 and pressed_old== 1:  #button is pressed which is a 0
            # if led is off turn led on (0) and is on turn off (1) so pass led = 0
            led = btn_switch(outPin, led)
        #if pressed==1:
        #    led = btn_switch(outPin, led)
        sleep(delay)
except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO ready to go")