#!/bin/bash/python3.5

from flask import Flask, render_template, request, jsonify
import getIpAddress
import blinktControl

app = Flask(__name__)

blinkt = [
	{'id': 0, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 1, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 2, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 3, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 4, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 5, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 6, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
	{'id': 7, 'brightness': 0.1, 'color': '#FFFFFF', 'state': False },
]


# HTTP pages
#@app.route('/', methods=['GET'])
#def index():
#	if request.args.get('LedOn'):
#		led = int(request.args.get('number'))
#		blinktControl.setLed(led - 1)
#		status = "LED %d turned on" % led
#	elif request.args.get('LedOff'):
#		led = int(request.args.get('number'))
#		blinktControl.clearLed(led - 1)
#		status = "LED %d turned off" % led
#	elif request.args.get('allOff'):
#		blinktControl.clearAll()
#		status = "All LEDs turned off"
#	elif request.args.get('allOn'):
#		blinktControl.setAll()
#		status = "All LEDs turned on"
#	else:
#		print('no idea...')
#		status = ""
#
#	return render_template('index.html', status=status)

# RESTful API
@app.route('/blinkt', methods=['GET'])
def blinkt_test():
	return jsonify(blinkt)

@app.route('/blinkt/<led>/<state>', methods=['GET'])
def set_blinkt_state(led, state):
	if int(led) in range(0, 8):
		if int(state) == 0:
			blinktControl.clearLed(int(led))
		else:
			blinktControl.setLed(int(led), 0.1, '#FF0000', True)
	return jsonify(blinkt) # Need to send response based on successful request

@app.route('/blinkt/<led_id>', methods=['PUT'])
def update_blinkt(led_id):
	led = blinkt[int(led_id)]
#	print(request.form)
	blinkt[int(led_id)]['brightness'] = float(request.form.get('brightness'))
	blinkt[int(led_id)]['color'] = request.form.get('color')
	blinkt[int(led_id)]['state'] = request.form.get('state')
	blinktControl.setLed(int(led_id), blinkt[int(led_id)]['brightness'], blinkt[int(led_id)]['color'], blinkt[int(led_id)]['state'])
	return jsonify(blinkt)

@app.route('/blinkt/all', methods=['PUT'])
def update_blinkt_all():
	print(request.form.get)
	for led in blinkt:
		led['brightness'] = float(request.form.get('brightness'))
		led['color'] = request.form.get('color')
		led['state'] = request.form.get('state')
		blinktControl.setAll(led['brightness'], led['color'], led['state'])
	return jsonify(blinkt)

# Local methods and runnint the app
ipaddr = getIpAddress.IpAddress()
print(ipaddr)

if __name__ == "__main__":
	app.run(debug=True, host=ipaddr, port=5000)
