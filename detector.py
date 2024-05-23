import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
#GPIO.setup(27, GPIO.IN)
#digital read pin
#clockspeed = 10
#GPIO.setup(3, GPIO.OUT)

def runForValues():
    pos = 0
    detectorvalues = [0,0,0]
    detectorvalues[0] = GPIO.input(14)
    detectorvalues[1] = GPIO.input(15)
    detectorvalues[2] = GPIO.input(18)

    #    for x in range(3):
#        detectorvalues[x] = GPIO.input(27)
#        clockpinupdate()
#        time.sleep(1/clockspeed)
#    
    if(detectorvalues[0] != 0 or detectorvalues[1] != 0 or detectorvalues[2] != 0):
        pos = detectorvalues[2]*4 + detectorvalues[1]*2 + detectorvalues[0]*1
    return pos
    
