#!/usr/bin/python3
from flask import Flask, render_template, request
from gpiozero import Device,Pin,OutputDevice

app = Flask(__name__)
pump = OutputDevice(21)

@app.route("/", methods=['GET','POST'])
def index():
    print(request.form)
    return render_template('index.html')

'''
@app.route("/pump", methods=['GET'])
def pump():
    print(request.get_json())
    return render_template('index.html')
'''
