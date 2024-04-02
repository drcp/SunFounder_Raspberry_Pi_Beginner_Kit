#Copy of McWhorter's code which works better because it doesn't blink when button is held, why?
#Switch around line 18 with the buttonState and buttonStateOld values. When switched the button lights led when up
import RPi.GPIO as GPIO 
from time import sleep
delay = 1
inPin=40
outPin=11 #change back to 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonState=1
buttonStateOld=1
LEDstate=0   #using pull_up resistor, led is off b/c PUD is not seeing ground
try:
    while True:
        buttonState=GPIO.input(inPin)
        print(buttonState)
        if buttonState==0 and buttonStateOld==1:
            LEDstate = not LEDstate
            GPIO.output(outPin,LEDstate)
        buttonStateOld=buttonState
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO is good')