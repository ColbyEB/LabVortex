import RPi.GPIO as GPIO
import time

pwm_high_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_high_pin, GPIO.OUT)

outt = 9 #tune
inn = 5 #tune


pwm_high = GPIO.PWM(pwm_high_pin, 50)  # 344 Hz frequency

pwm_high.start(0)

def test():
    x = 0
    while True:
        pwm_high.ChangeDutyCycle(x)
        print(x)
        x = x + 1
        time.sleep(.3)


def out():
    pwm_high.ChangeDutyCycle(outt)
    time.sleep(1.6)

def reverse():
    pwm_high.ChangeDutyCycle(inn)
    time.sleep(1.6)
