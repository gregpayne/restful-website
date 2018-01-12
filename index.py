#!/bin/bash/python3.5

from flask import Flask, render_template, request, jsonify
import getIpAddress
import blinktControl

app = Flask(__name__)

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
@app.route('/blinkt', methods=['GET'])
def blinkt_test():
	return jsonify(blinkt)

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
