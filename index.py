#!/bin/bash/python3.5

from flask import Flask, render_template, request
import getIpAddress
import blinktControl

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	if request.args.get('LedOn'):
		led = int(request.args.get('number')) - 1
		blinktControl.setLed(led)
		status = "LED %d turned on" % led
	elif request.args.get('LedOff'):
		led = int(request.args.get('number')) - 1
		blinktControl.clearLed(led)
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

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	return render_template('hello.html', name=name)

ipaddr = getIpAddress.IpAddress()
print(ipaddr)

if __name__ == "__main__":
	app.run(debug=True, host=ipaddr, port=5000)
