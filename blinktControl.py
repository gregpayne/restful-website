#!/bin/bash/python3.5

import blinkt
import time
from colormap.colors import hex2rgb

def setLed(led, brightness, color, state):
	if state == "true":
		blinkt.set_brightness(brightness) # set the brightness between 0 and 1
		blinkt.set_pixel(led, getR(color), getG(color), getB(color))
		blinkt.show()
	else:
		clearLed(led)

def clearLed(led):
	blinkt.set_pixel(led, 0, 0, 0)
	blinkt.show()

def setAll(brightness, color, state):
	for i in range(8):
		setLed(i, brightness, color, state)

#def clearAll():
#	for i in range(8):
#		setLed(i, brightness, color, False)
#	blinkt.show()

def getR(color):
	c = hex2rgb(color, normalise=False)
	return c[0]

def getG(color):
	c = hex2rgb(color, normalise=False)
	return c[1]

def getB(color):
	c = hex2rgb(color, normalise=False)
	return c[2]


