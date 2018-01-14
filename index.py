#!/bin/bash/python3.5

from flask import Flask, render_template, request, jsonify
import getIpAddress
import blinktControl

app = Flask(__name__)

# Default Blinkt startup configuration
# TODO: This could be moved to a database instead of being hardcoded
blinkt = [
	{'id': 0, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 1, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 2, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 3, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 4, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 5, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 6, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
	{'id': 7, 'brightness': 0.1, 'color': '#FFFFFF', 'state': 'false' },
]


# RESTful API
@app.route('/blinkt/init', methods=['PUT']) # Has to be PUT as the Android App send a PUT
def blinkt_test():
	return jsonify(blinkt)

@app.route('/blinkt/<led_id>', methods=['PUT'])
def update_blinkt(led_id):
	led = blinkt[int(led_id)]
	blinkt[int(led_id)]['brightness'] = request.form.get('brightness')
	blinkt[int(led_id)]['color'] = request.form.get('color')
	blinkt[int(led_id)]['state'] = request.form.get('state')
	blinktControl.setLed(int(led_id), blinkt[int(led_id)]['brightness'], blinkt[int(led_id)]['color'], blinkt[int(led_id)]['state'])
	return jsonify(blinkt)

@app.route('/blinkt/all', methods=['PUT'])
@app.route('/blinkt/color', methods=['PUT'])
@app.route('/blinkt/brightness', methods=['PUT'])
def update_blinkt_all():
	if 'all' in request.url:
		for led in blinkt:
			led['brightness'] = float(request.form.get('brightness'))
			led['state'] = request.form.get('state')
			led['color'] = request.form.get('color')
		blinktControl.setAll(led['brightness'], led['color'], led['state'])

	if 'color' in request.url:
		for led in blinkt:
			led['color'] = request.form.get('color')
			blinktControl.setLed(led['id'], led['brightness'], led['color'], led['state'])

	if 'brightness' in request.url:
		for led in blinkt:
			led['brightness'] = float(request.form.get('brightness'))
			blinktControl.setLed(led['id'], led['brightness'], led['color'], led['state'])

	return jsonify(blinkt)

# Local methods and runnint the app
ipaddr = getIpAddress.IpAddress()
print(ipaddr)

if __name__ == "__main__":
	app.run(debug=True, host=ipaddr, port=5000)
