# McWhorton used a log value to step ou LEDs
# Three color buttons which step up to ~10 then reset to zero 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# setup input/out pins
rPin=11
gPin=13
bPin=12
rBut=40
gBut=38
bBut=37

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.setup(rBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)

myPWMr=GPIO.PWM(rPin,100)
myPWMg=GPIO.PWM(gPin,100)
myPWMb=GPIO.PWM(bPin,100)
# set duty cycle to .99 so with int method it registers as zero
DCr=.99
DCg=.99
DCb=.99
# delay time
dt=.1
# open channel to LED
myPWMr.start(int(DCr))
myPWMg.start(int(DCg))
myPWMb.start(int(DCb))
#setup variables to track button state
rButState, rButStateOld =0, 0
gButState, gButStateOld =0, 0
bButState, bButStateOld =0, 0

def red_func(myPWMr, DCr, rButState, rButStateOld):
    if rButState==1 and rButStateOld==0:
        DCr=DCr*1.58
        print('Red channel registered')
        if DCr>99:
            DCr=.99
        myPWMr.ChangeDutyCycle(int(DCr))
    return DCr
def green_func(myPWMg, DCg, gButState, gButStateOld):
    if gButState==1 and gButStateOld==0:
        DCg=DCg*1.58
        print('Green channel registered')
        if DCg>99:
            DCg=.99
        myPWMg.ChangeDutyCycle(int(DCg))
    return DCg
def blue_func(myPWMb, DCb, bButState, bButStateOld):
    if bButState==1 and bButStateOld==0:
        DCb=DCb*1.58
        print('Blue channel registered')
        if DCb>99:
            DCb=.99
        myPWMb.ChangeDutyCycle(int(DCb))
    return DCb
try:
    while True:
        # Capture current button states
        rButState=GPIO.input(rBut)
        gButState=GPIO.input(gBut)
        bButState=GPIO.input(bBut)
        print('Button state: '+ "rButState,gButState,bButState")
        # running button checks a functions for clarity
        DCr = red_func(myPWMr, DCr, rButState, rButStateOld)
        DCg = green_func(myPWMg, DCg, gButState, gButStateOld)
        DCb = blue_func(myPWMb, DCb, bButState, bButStateOld)
# store previous button states
        rButStateOld=rButState
        gButStateOld=gButState
        bButStateOld=bButState
        print("duty cycles: "+str(DCr),str(DCg),str(DCb))
        time.sleep(dt)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nGPIO good to go\n")