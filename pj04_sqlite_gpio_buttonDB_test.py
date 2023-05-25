import sqlite3
import RPi.GPIO as gpio
import time
import datetime as dt

gpio.setmode(gpio.BCM) #OR GPIO.BOARD
BUTTON = 4
LED = 18

ledStates = 0

gpio.setup(BUTTON, gpio.IN, pull_up_down = gpio.PUD_UP) # pushbutton
gpio.setup(LED, gpio.OUT) # led
gpio.output(LED, False)

countButtonDown = 0

while(True):
    valPushButton = gpio.input(BUTTON)
    if(valPushButton == True): # up!
        gpio.output(LED, True) # LED ON
        countButtonDown = countButtonDown + 1
        print("CountButtonDown = %d, DatetimeNow = %s" % (countButtonDown, dt.datetime.now()))
        # CREATE with INSERT statement
        conn = sqlite3.connect('/home/[USER NAME]/python/DB/buttonDB.db')
        c = conn.cursor()
        c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, datetime('now','localtime'))", ('on', 1))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('/home/[USER NAME]/python/DB/buttonDB.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bStatesTable")
        results = c.fetchall()
        conn.close()        
        
        print("SELECT DB results: \n", results)
        time.sleep(1)