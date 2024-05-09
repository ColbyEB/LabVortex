import RPi.GPIO as GPIO

pwm_high_pin = 6 # not right pin YET
pwm_low_pin = 9 # ALSO NOT RIGHT PIN PLEASE CONFIGURE

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_high_pin, GPIO.OUT)
GPIO.setup(pwm_low_pin, GPIO.OUT)

pwm_high = GPIO.PWM(pwm_high_pin, 100)  # 344 Hz frequency
pwm_low = GPIO.PWM(pwm_low_pin, 100)    # 1000 Hz frequency

def pwmStartFwd():
    pwm_high.stop()
    pwm_low.stop()
    pwm_high.start(6)  # Start PWM with 6% duty cycle
    pwm_low.start(0)   # Start PWM with 0% duty cycle

def pwmStartReverse():
    pwm_high.stop()
    pwm_low.stop()
    pwm_high.start(0)  # Start PWM with 6% duty cycle
    pwm_low.start(6)   # Start PWM with 0% duty cycle


