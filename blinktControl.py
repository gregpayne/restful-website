#!/bin/bash/python3.5

import blinkt
import time
from colormap.colors import hex2rgb

def setLed(led, brightness, color):
	blinkt.set_brightness(brightness) # set the brightness between 0 and 1
	blinkt.set_pixel(led, getR(color), getG(color), getB(color))
	blinkt.show()

def clearLed(led):
	blinkt.set_pixel(led, 0, 0, 0)
	blinkt.show()

def setAll(brightness, color):
	blinkt.set_brightness(brightness) # set the brightness between 0 and 1
	for i in range(8):
		blinkt.set_pixel(i, getR(color), getG(color), getB(color))
	blinkt.show()

def clearAll():
	blinkt.set_brightness(brightness) # set the brightness between 0 and 1
	blinkt.clear()
	blinkt.show()

def getR(color):
	c = hex2rgb(color, normalise=False)
	return c[0]

def getG(color):
	c = hex2rgb(color, normalise=False)
	return c[1]

def getB(color):
	c = hex2rgb(color, normalise=False)
	return c[2]


