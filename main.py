import RPi.GPIO as GPIO
import detector
from threading import thread 

detectorpos
thread = detector.runForValues
thread.start()

while True:
    if(detector.detectorvalues[0] != 0 | detector.detectorvalues[1] != 0 | detector.detectorvalues[2] != 0):
        detectorpos = detector.detectorvalues[2] * 4 + detector.detectorvalues[1] * 2 + detector.detectorvalues