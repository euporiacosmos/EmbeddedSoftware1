import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # pushButton
GPIO.setup(18, GPIO.OUT) # LED(red)

countButtonDown = 0
old_valPushButton = True

while(True):
    valPushButton = GPIO.input(4)
    if(valPushButton == True): # up!
        GPIO.output(18, False) # LED OFF
    
    elif((valPushButton == False) and (old_valPushButton == True)): # down!
        GPIO.output(18, True) # LED ON
        countButtonDown = countButtonDown + 1 # '+=' does not work
    
    old_valPushButton = valPushButton
    time.sleep(0.1)
    
    # print("Value of PushButton= ", valPushButton)
    print("CountButtonDown = ", countButtonDown)