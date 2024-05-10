import RPi.GPIO as GPIO
import detector
from threading import thread 


thread = detector.runForValues
thread.start()

while True:
    print(detector.position)
