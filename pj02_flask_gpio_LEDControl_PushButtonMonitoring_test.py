from flask import Flask, render_template, request
from pj02_flask_gpio_html_gpioControl import *

app = Flask(__name__, template_folder='.')

@app.route('/')
def do_route():
    init()
    valPushButton = readButton()
    return render_template("pj02_flask_gpio_html_index.html", btnState=valPushButton)

#control rccar
@app.route('/led', methods=['POST'])
def control_led():
    command=request.form.get('command')
    #print(command)
    if command == "ledON":
        ledOn()
    elif command == "ledOFF":
        ledOff()
    return ''


if __name__ == '__main__': # Program start from here
    app.run(host='[IP Address]', port=[PORT NUMBER])
