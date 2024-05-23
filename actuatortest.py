import RPi.GPIO as GPIO
import time

pwm_high_pin = 13 # not right pin YET

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_high_pin, GPIO.OUT)


pwm_high = GPIO.PWM(pwm_high_pin, 50)  # Hz frequency

pwm_high.start(5)

def test():
    #pwm_high.ChangeDutyCycle(5)
    #time.sleep(5)
    
    x = 5
    while True:
        while x < 10:
            pwm_high.ChangeDutyCycle(x)
            print(x)
            x = x + .33
            time.sleep(.1)
        while x > 5:
            pwm_high.ChangeDutyCycle(x)
            print(x)
            x = x - .33
            time.sleep(.1)


def test2():
    while True:
        pwm_high.ChangeDutyCycle(5)
        time.sleep(4)
        pwm_high.ChangeDutyCycle(10)
        time.sleep(4)
        #time.sleep(.02)
        #GPIO.output(16, GPIO.LOW)
        #time.sleep(.001)


test2()
