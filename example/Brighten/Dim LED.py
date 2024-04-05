import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) 
#PWM -  Pulse Width Modulation. !! First line p = the PWM freq of 50 !! Later p can change the PWM or how long the pulse/LED is on during a cycle 
p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz. changed from 12 to 40
p.start(0) # p.
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()