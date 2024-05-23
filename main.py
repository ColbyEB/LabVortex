import RPi.GPIO as GPIO
import detector
import turntablecontroller
import threading
import time
import actuator
import shaftcim

#x = threading.Thread(target = detector.runForValues, args=())
#x.start()
def main():
    print("testing?")
    x = input()
    if(x == "y"):
        test()
    else:
        mainLoop()

def mainLoop():
    while True:
        print("what value would you like to go to")
        value = input()
        while True:
            position = detector.runForValues()
            print(position)
            print(value)
            if (position == int(value)):
                break
            else:
                turntablecontroller.fwd()
        turntablecontroller.off()
        shaftcim.down()
        print("how many times")
        x = input()
        number = int(x)
        for i in range(number):
            actuator.out()
            actuator.reverse()
        shaftcim.up()




            
def test():
    turntablecontroller.fwd()
    time.sleep(5)
    turntablecontroller.reverse()
    time.sleep(5)
    turntablecontroller.off()
    


main()
