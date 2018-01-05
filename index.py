#!/bin/bash/python3.5

from flask import Flask, render_template
import getIpAddress

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	return render_template('hello.html', name=name)


ipaddr = getIpAddress.IpAddress()
print(ipaddr)

if __name__ == "__main__":
	app.run(debug=True, host=ipaddr, port=5000)
