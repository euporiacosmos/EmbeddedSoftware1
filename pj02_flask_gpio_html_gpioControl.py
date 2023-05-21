import RPi.GPIO as GPIO

# constant is better than variable this case
BUTTON = 4
RED = 18

def initLeds():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Pin input setup
    GPIO.setup(BUTTON, GPIO.IN)

    # Pin output setup
    GPIO.setup(RED, GPIO.OUT)

def redOn():
    GPIO.output(RED, True)

def redOff():
    GPIO.output(RED, False)

def readButton():
    return GPIO.input(BUTTON)