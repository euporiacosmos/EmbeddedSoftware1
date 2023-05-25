import RPi.GPIO as gpio

# constant is better than variable this case
BUTTON = 4
LED = 18

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)

    # Pin input setup
    gpio.setup(BUTTON, gpio.IN, pull_up_down = gpio.PUD_UP)

    # Pin output setup
    gpio.setup(LED, gpio.OUT)

def ledOn():
    gpio.output(LED, True)

def ledOff():
    gpio.output(LED, False)

def readButton():
    return gpio.input(BUTTON)