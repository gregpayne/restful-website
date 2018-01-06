#!/bin/bash/python3.5

from flask import Flask, render_template, request, jsonify
import getIpAddress
import blinktControl

app = Flask(__name__)

# HTTP pages
@app.route('/', methods=['GET'])
def index():
	if request.args.get('LedOn'):
		led = int(request.args.get('number'))
		blinktControl.setLed(led - 1)
		status = "LED %d turned on" % led
	elif request.args.get('LedOff'):
		led = int(request.args.get('number'))
		blinktControl.clearLed(led - 1)
		status = "LED %d turned off" % led
	elif request.args.get('allOff'):
		blinktControl.clearAll()
		status = "All LEDs turned off"
	elif request.args.get('allOn'):
		blinktControl.setAll()
		status = "All LEDs turned on"
	else:
		print('no idea...')
		status = ""

	return render_template('index.html', status=status)

# RESTful API
@app.route('/blinkt', methods=['GET'])
def blinkt_test():
	return jsonify({'tasks': tasks})

@app.route('/blinkt/<led>/<state>', methods=['GET'])
def set_blinkt_state(led, state):
	if int(led) in range(0, 8):
		if int(state) == 0:
			blinktControl.clearLed(int(led))
		else:
			blinktControl.setLed(int(led))
	return jsonify() # Need to send response based on successful request

# Local methods and runnint the app
ipaddr = getIpAddress.IpAddress()
print(ipaddr)

if __name__ == "__main__":
	app.run(debug=True, host=ipaddr, port=5000)
