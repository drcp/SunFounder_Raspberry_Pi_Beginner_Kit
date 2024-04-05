import RPi.GPIO as GPIO
from time import sleep
dt = .1
 
rPin = 11
gPin = 13
bPin = 12
 
rBut = 40
gBut = 38
bBut = 37
 
rButState = 1
rButStateOld = 1
 
gButState = 1
gButStateOld = 1
 
bButState = 1
bButStateOld = 1
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
 
GPIO.setup(rBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
myPWMr = GPIO.PWM(rPin, 100)
myPWMg = GPIO.PWM(gPin, 100)
myPWMb = GPIO.PWM(bPin, 100)
 
DCr = .99
DCg = .99
DCb = .99
 
myPWMr.start(int(DCr))
myPWMg.start(int(DCg))
myPWMb.start(int(DCb))
 
try:
    while True:
        rButState = GPIO.input(rBut)
        gButState = GPIO.input(gBut)
        bButState = GPIO.input(bBut)
        print('Button State', rButState, gButState, bButState)
        if rButState == 1 and rButStateOld == 0:
            DCr = DCr*1.58
            print('Red Channel Registered')
            if DCr > 99:
                DCr = .99
            myPWMr.ChangeDutyCycle(int(DCr))
        if gButState == 1 and gButStateOld == 0:
            DCg = DCg*1.58
            print('Green Channel Registered')
            if DCg > 99:
                DCg = .99
            myPWMg.ChangeDutyCycle(int(DCg))
        if bButState == 1 and bButStateOld == 0:
            DCb = DCb*1.58
            if DCb > 99:
                DCb = .99
            myPWMb.ChangeDutyCycle(int(DCb))
        rButStateOld = rButState
        gButStateOld = gButState
        bButStateOld = bButState
        print(DCr, DCg, DCb)
        sleep(dt)
except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print('GPIO Good to Go')