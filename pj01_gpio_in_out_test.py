import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM) # BCM standard is made by a compny while BOARD standard is embed in RPi itself.
gpio.setup(4, gpio.IN) # pushButton
gpio.setup(18, gpio.OUT) # LED(red)

countButtonDown = 0
old_valPushButton = True

while(True):
    valPushButton = gpio.input(4)
    if(valPushButton == True): # up!
        gpio.output(18, False) # LED OFF
    
    elif((valPushButton == False) and (old_valPushButton == True)): # down!
        gpio.output(18, True) # LED ON
        countButtonDown = countButtonDown + 1 # '+=' does not work
    
    old_valPushButton = valPushButton
    time.sleep(0.1)
    
    # print("Value of PushButton= ", valPushButton)
    print("CountButtonDown = ", countButtonDown)