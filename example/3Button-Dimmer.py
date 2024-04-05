# Three buttons red, blue and green; when pressed as a toggle switch turn
# on or off that LED. Similar to the toggleLED script. 
import RPi.GPIO as GPIO
import time
delay= .1
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
global redLEDstate
redLEDstate=0
bRedState = 0
bRedStateOld = False
#global blueLEDstate
blueLEDstate=0
bBlueState = 0
bBlueStateOld = False
#global greenLEDstate
greenLEDstate=0
bGreenState = 0
bGreenStateOld = False

# New section added for new features: each button should dim it's LED by stepping up 10% to 99% then go to zero with next press starting over.
bPWM = GPIO.PWM(12,100) # Blue pin 12 and freq of 100
rPWM = GPIO.PWM(11,100) # Red pin 11, same freq
gPWM = GPIO.PWM(13,100) # Green pin 13, same freq

# Start PWMs for all three
bPWM.start(50)
rPWM.start(50)
gPWM.start(50)


# In main loop in from buttons -> change DC(duty cycle) with a function
# myPWM.ChangeDutyCycle(75)
# myPWM.ChangeFrequency(33)

""" #Get from pin 40 duty cycle
def set_led_value(value):    # Define a function 
    PWM.ChangeDutyCycle(100-value)
 """    
#Get from pin 37 frequency
#Function to set duty cycle and frequency
""" def set_duty_freq(duty,freq):
    GPIO.PWM(40,duty)
 """
# function to step rLED up till it goes past 100 then goes to 0
def rStepLED(redLEDstate):
    global redLEDstate
    #if x is between 0 - 100 step up if > 100 go to zero
    # x is the DC
    redLEDstate = 10 + redLEDstate
    if redLEDstate < 101:
# After the increment Light the LED with the DC
        rPWM.ChangeDutyCycle(redLEDstate)
    else:
        redLEDstate = 0
        rPWM.ChangeDutyCycle(redLEDstate)
    return(redLEDstate)

# function to step bLED up til goes past 100 then goes to 0
def bStepLED(x):
    #if x is between 0 - 100 step up if > 100 go to zero
    if x < 101:
        bPWM.ChangeDutyCycle(x)
        x = 10 + x
    else:
        x = 0
    return(x)

# function to step gLED up til goes past 100 then goes to 0
def gStepLED(x):
    #if x is between 0 - 100 step up if > 100 go to zero
    if x < 101:
        gPWM.ChangeDutyCycle(x)
        x = 10 + x
    else:
        x = 0
    return(x)

# start while loop
# listening for r,g,b button press
# send signal to function to step r,g or b button up a step in DC
# red function to step LED and check for valid values
def red_func(rPin, redLEDstate, bRedState, rPWM, rStepLED):

    bRedState = GPIO.input(rPin)
    print("red LED state: "+ str(redLEDstate))        

    print("button red state: "+ str(bRedState))  

    # if bRedState == 0:
        # redLEDstate = redLEDstate + 10
    if redLEDstate > 100:
        redLEDstate = 0
        # rPWM.ChangeDutyCycle(redLEDstate)        
        rStepLED(redLEDstate)
    else:
        rStepLED(redLEDstate)
        # rPWM.ChangeDutyCycle(redLEDstate)
        # rStepLED(redLEDstate)
        print("red LED state: " + str(redLEDstate))    
# Blue
def blue_func(bPin, blueLEDstate, bBlueState, bPWM, bStepLED):
    print("button blue state: "+ str(bBlueState))        
    bBlueState = GPIO.input(bPin)
    if bBlueState == 0:
        blueLEDstate = blueLEDstate + 10
    if blueLEDstate > 100:
        blueLEDstate = 0
        bPWM.ChangeDutyCycle(blueLEDstate)
    else:
        bStepLED(blueLEDstate)
        bPWM.ChangeDutyCycle(blueLEDstate)

# Green
def green_func(gPin, greenLEDstate, bGreenState, gPWM, gStepLED):
    print("button Green state: "+ str(bGreenState))        
    bGreenState = GPIO.input(gPin)
    if bGreenState == 0:
        greenLEDstate = greenLEDstate + 10
    if greenLEDstate > 100:
        greenLEDstate = 0
        gPWM.ChangeDutyCycle(greenLEDstate)
    else:
        gStepLED(greenLEDstate)
        gPWM.ChangeDutyCycle(greenLEDstate)

try:
    while True:
        red_func(rPin, redLEDstate, bRedState, rPWM, rStepLED)
        
        blue_func(bPin, blueLEDstate, bBlueState, bPWM, bStepLED)
        
        green_func(gPin, greenLEDstate, bGreenState, gPWM, gStepLED)
        time.sleep(delay)
except KeyboardInterrupt:
    rPWM.stop()
    bPWM.stop()
    gPWM.stop()
    GPIO.cleanup()
    print("Alls good in the neighborhood")


