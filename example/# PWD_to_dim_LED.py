# PWD_to_dim_LED
# Pin #12 is GPIO.OUT to power LED
# pin #40 is a GPIO.IN to check duty cycle
# Pin #37 is a GPIO>IN to check freguency
# Pin #39 is ground

import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN)
GPIO.setup(40,GPIO.IN)



PWM = GPIO.PWM(37,100)
# myPWM.start(50)
# myPWM.ChangeDutyCycle(75)
# myPWM.ChangeFrequency(33)

#Get from pin 40 duty cycle
def set_led_value(value):    # Define a function 
    PWM.ChangeDutyCycle(100-value)
    
#Get from pin 37 frequency
#Function to set duty cycle and frequency
def set_duty_freq(duty,freq):
    GPIO.PWM(40,duty)
