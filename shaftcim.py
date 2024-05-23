import time
import RPi.GPIO as GPIO

pwm_high_pin = 20 # not right pin YET
pwm_low_pin = 21 # ALSO NOT RIGHT PIN PLEASE CONFIGURE

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_high_pin, GPIO.OUT)
GPIO.setup(pwm_low_pin, GPIO.OUT)

pwm_high = GPIO.PWM(pwm_high_pin, 100)  # 344 Hz frequency
pwm_low = GPIO.PWM(pwm_low_pin, 100)    # 1000 Hz frequency
pwm_high.start(0)
pwm_low.start(0)

def down():
    print("down")
    pwm_high.ChangeDutyCycle(16)  # Start PWM with 6% duty cycle
    time.sleep(1)
    pwm_high.ChangeDutyCycle(0)   # Start PWM with 0% duty cycle
    
def up():
    print("up")
    pwm_high.ChangeDutyCycle(11)  # Start PWM with 6% duty cycle
    time.sleep(2)
    pwm_high.ChangeDutyCycle(0)   # Start PWM with 0% duty cycle
