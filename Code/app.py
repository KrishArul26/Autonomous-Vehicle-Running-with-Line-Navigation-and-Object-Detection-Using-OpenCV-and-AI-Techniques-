#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from flask.helpers import make_response
import json
import time
import cv2
from Motor import *
from Buzzer import *
from Led import *
from ADC import *
from Servo import *
from lane_detection import *

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera
from camera_opencv import Camera

adc = Adc()
led = Led()
Buz = Buzzer()
PWM = Motor()
SRV = Servo()
steering = -90
autopilot = 0  
stop = False

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        try:
           
            combine_image, heading_image = detect_lane3(frame)
           
            image = cv2.imencode('.jpg', heading_image)[1].tobytes()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
        except TypeError:
            pass

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_img')
def capture_img():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    response = make_response(Camera().get_frame())
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename=f"img_{timestr}.jpg")
    return response


@ app.route('/forward')
def drive_forward():
    Buz.run('0')
    # car.run('0')
    # left, right, reft correction, right correction
    PWM.setMotorModel(40, 40)  # Forward
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/back')
def drive_back():
    #car.run('1')
    PWM.setMotorModel(-40, -40)  # Back
    Buz.run('1')
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/left')
def drive_left():
    #car.run('0')
    led.blink('l', 255, 215, 0)
    led.blink('r', 0, 0, 0)
    SRV.setServoPwm('4', 135)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/right')
def drive_right():
    led.blink('r', 255, 215, 0)
    led.blink('l', 0, 0, 0)
    SRV.setServoPwm('4', 45)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/stop_turn')
def stop_turn():
    led.colorWipe(led.strip, Color(0, 0, 0), 10)
    SRV.setServoPwm('4', 90)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/stop')
def drive_stop():
    global stop
    Buz.run('0')
    stop = True
    PWM.setMotorModel(0, 0)
    led.colorWipe(led.strip, Color(0, 0, 0), 10)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@ app.route('/pwr')
def get_voltage():
    return json.dumps(adc.getPower())


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=80)


