#!/bin/bash/python3.5

import blinkt
import time

def setLed(led):
	blinkt.set_brightness(0.1) # set the brightness between 0 and 1
	blinkt.set_pixel(led, 255, 255, 255)
	blinkt.show()

def clearLed(led):
	blinkt.set_brightness(0.1) # set the brightness between 0 and 1
	blinkt.set_pixel(led, 0, 0, 0)
	blinkt.show()

def setAll():
	blinkt.set_brightness(0.1) # set the brightness between 0 and 1
	for i in range(8):
		blinkt.set_pixel(i, 255, 255, 255)
	blinkt.show()

def clearAll():
	blinkt.set_brightness(0.1) # set the brightness between 0 and 1
	blinkt.clear()
	blinkt.show()



