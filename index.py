#!/bin/bash/python3.5

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	return render_template('hello.html', name=name)
