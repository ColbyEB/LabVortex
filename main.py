import RPi.GPIO as GPIO
import detector
import threading 


x = threading.Thread(target = detector.runForValues, args=())
x.start()

while True:
    detector.runForValues()
    print(detector.position)
