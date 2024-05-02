import RPi.GPIO as GPIO
import linefollower.py as detector
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
#digital read pin

GPIO.setup(3, GPIO.OUT)

def clockpinupdate():
    GPIO.output(3, GPIO.HIGH)
    wait(.001)
    GPIO.output(3, GPIO.LOW)
    
class muxdetector:
    def __init__(self, clockspeed, numdetectors):
        self.clockspeed = clockspeed
        self.numdetectors = numdetectors

    def setup:
        self.detectors[self.numdetectors]
        for x in self.numdetectors:
            detectors[x] = detector(x, x)
    def clock(clockspeed):
        self.digitalvalues[numdetectors]
        while True:
            #something about clockspeed something modulus
            for x in numdetectors:
                digitalvalues[x] = detectors[x].getValue()
            clockpinupdate()
            wait(1/clockspeed)
            print(self.digitalvalues)
        




