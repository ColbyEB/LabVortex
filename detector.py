import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
#digital read pin
clockspeed = 10
GPIO.setup(3, GPIO.OUT)

def clockpinupdate():
    GPIO.output(3, GPIO.HIGH)
    time.sleep(.001)
    GPIO.output(3, GPIO.LOW)
    
    
detectorvalues = [0,0,0]
def runForValues():
    while True:
        for x in range(3):
            detectorvalues[x] = GPIO.input(27)
            clockpinupdate()
        time.sleep(1/clockspeed)
        print(detectorvalues)
