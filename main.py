#!/usr/bin/python3
from flask import Flask, render_template, request
from gpiozero import Device,Pin,OutputDevice

PIN = 21

app = Flask(__name__, static_url_path='/static')
pump = OutputDevice(PIN)


@app.route('/', methods=["GET","POST"])
def index():
    turn_on = False
    if request.method == "POST":
        if "pump" in request.form:
            print("Turn pump on")
            turn_on = True
            pump.on()
        else:
            print("Turn pump off")
            pump.off()
        print(pump.value)

    return render_template("index.html", state="checked=checked" if turn_on else "")


if __name__ == "__main__":  
    #app.run(host="0.0.0.0",debug=True)
	app.run()
