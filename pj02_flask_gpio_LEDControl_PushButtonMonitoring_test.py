from flask import Flask, render_template_string
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
BUTTON = 4 # constant is better than variable this case
LED = 18
ledStates = 0
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)

app = Flask(__name__)

def updateLed():
    GPIO.output(LED, ledStates)

control_page = '''
    <script>
    function changed(id)
    {
        window.location.href='/' + id;
    }
    </script>
    <h1>GPIO Monitor-PushButton/Control-LED</h1>
    <h2>Button State
    {% if btnState %}
    =Up
    {% else %}
    =Down
    {% endif %}
    </h2>
    <input type="button" onClick="changed({[1]})" value='LED on'>
    <input type="button" onClick="changed({[0]})" value='LED off'>
    <meta http-equiv="refresh" content="1">
    '''

@app.route('/')
def index(led='n'): # GET REQUEST
    global ledStates

    print('led=', led)

    if led != 'n' and led != 'favicon.ico':
        led = int(led)
        if(led):
            ledStates = True
        else:
            ledStates = False

        print('ledStates=', ledStates)
        GPIO.output(LED, ledStates)

    valPushButton = GPIO.input(BUTTON)
    return render_template_string(control_page, btnState=valPushButton)

if __name__ == '__main__': # Program start from here
    app.run(host='192.168.0.2', port=8080)