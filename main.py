#!/usr/bin/python3
from flask import Flask
from gpiozero import Device,Pin,OutputDevice

app = Flask(__name__)
pump = OutputDevice(21)

@app.route("/")
def index():
    return "Hi"

@app.route("/pump")
def pump():
    return pump.value
