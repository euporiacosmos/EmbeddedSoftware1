import sqlite3
import RPi.GPIO as gpio
import time
import datetime as dt

gpio.setmode(gpio.BCM) #OR GPIO.BOARD
BUTTON = 4
LED = 18

ledStates = 0

gpio.setup(BUTTON, gpio.IN) # pushbutton
gpio.setup(LED, gpio.OUT) # led
gpio.output(LED, False)

countButtonDown = 0
old_valPushButton = True

def main():
    global countButtonDown
    while(True):
        valPushButton = gpio.input(BUTTON)
        if(valPushButton == True): # up!
            gpio.output(LED, False) # LED OFF

        elif((valPushButton == False) and (old_valPushButton == True)): # down!
            gpio.output(LED, True) # LED ON
            countButtonDown = countButtonDown + 1
        print("CountButtonDown = %d, DatetimeNow = %s" % (countButtonDown, dt.datetime.now()))
        #============SQLite database ============
        conn = sqlite3.connect('/home/[USERNAME]/python/DB/buttonDB.db')
        c = conn.cursor()
        #c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, DATETIME('now'))", ('on', 1)) #ok
        #c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, datetime('now'))", ('on', 1)) #ok
        c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, datetime('now','localtime'))", ('on', 1))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('/home/[USERNAME]/python/DB/buttonDB.db')
        c = conn.cursor()
        #c.execute("SELECT * FROM bStatesTable WHERE date BETWEEN '2022-01-01 10:10:10' AND DATETIME('now')")
        c.execute("SELECT * FROM bStatesTable WHERE date BETWEEN '2022-04-01 0:0:0' AND DATETIME('now','localtime')")
        results = c.fetchall()
        conn.close()        
        #===
        print("SELECT DB results: \n", results)     
        old_valPushButton = valPushButton
        time.sleep(1)

if __name__ == '__main__':
    main()
