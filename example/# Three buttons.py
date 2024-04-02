# Three buttons red, blue and green; when pressed as a toggle switch turn
# on or off that LED. Similar to the toggleLED script. 
import RPi.GPIO as GPIO
from time import sleep
delay= 1
GPIO.setmode(GPIO.BOARD)
# Pins out to LED
# redinPin is 12, BLUEinPin is 13, GREENinPin is 14
REDoutPin=11 #Grey wire
BLUEoutPin=12 #Blue wire
GREENoutPin=13 #White wire
# Setup pin outputs to leds
GPIO.setup(REDoutPin,GPIO.OUT)
GPIO.setup(GREENoutPin,GPIO.OUT)
GPIO.setup(BLUEoutPin,GPIO.OUT)

# Pins in from buttons
bPin=37 #actually blue is pin 37
rPin=40 # so this must be red 40
gPin=38 #actually green is pin 38
#  setup the inputs from the buttons
GPIO.setup(rPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set current and past state of LEDs
bRedState = True
bRedStateOld = False
bBlueState = True
bBlueStateOld = False
bGreenState = True
bGreenStateOld = False


# setup loop to run button script.
try:
    while True:
        # if red button is pressed toggle rLED on/off
        # read red in pin
        bRedState = GPIO.input(rPin)
        print("button red state: "+ str(bRedState))
        if bRedState == True and bRedStateOld == False:
            # Output to turn on rLED on if off or reverse
            bRedStateOld = not bRedState
            GPIO.output(REDoutPin,bRedState)

            #Blue next
        bBlueState = GPIO.input(bPin)
        print("button blue state: "+ str(bBlueState))
        if bBlueState == 0 and bBlueStateOld == 1:
            # Output to turn on rLED on if off or reverse
            bRedStateOld = not bBlueState
            GPIO.output(BLUEoutPin,bBlueState)

            #Now green
        bGreenState = GPIO.input(gPin)
        print("button green state: "+ str(bGreenState))
        if bGreenState == 0 and bGreenStateOld == 1:
            # Output to turn on rLED on if off or reverse
            bGreenStateOld = not bGreenState  
            GPIO.output(GREENoutPin,bGreenState)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Alls good in the neighborhood")
