import RPi.GPIO as GPIO

pwm_high_pin = 19 # not right pin YET
pwm_low_pin = 26 # ALSO NOT RIGHT PIN PLEASE CONFIGURE

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_high_pin, GPIO.OUT)
GPIO.setup(pwm_low_pin, GPIO.OUT)

pwm_high = GPIO.PWM(pwm_high_pin, 100)  # 344 Hz frequency
pwm_low = GPIO.PWM(pwm_low_pin, 100)    # 1000 Hz frequency
pwm_high.start(0)
pwm_low.start(0)

def fwd():
    print("fwd")
    pwm_high.ChangeDutyCycle(14.95)  # Start PWM with 6% duty cycle
    pwm_low.ChangeDutyCycle(0)   # Start PWM with 0% duty cycle
def reverse():
    #center is 15
    print("reverse")
    pwm_high.ChangeDutyCycle(13.85)  # Start PWM with 6% duty cycle
    pwm_low.ChangeDutyCycle(0)   # Start PWM with 0% duty cycle
def off():
    print("off")
    pwm_high.ChangeDutyCycle(0)
    pwm_low.ChangeDutyCycle(0)


