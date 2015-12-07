#!/usr/bin/env python2

import RPi.GPIO as gpio
from time import sleep
import sys
import math
from spnav import *


spnav_open()

pin=10

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

pwm = gpio.PWM(pin, 50)
pwm.start(0)


srv_bnd=[3, 8]

b = 0.5
while True:
  event = spnav_poll_event()
  if isinstance(event, SpnavMotionEvent):
    rot = event.rotation[1]
    b = (rot + 350.0) / 700.0
  b = max(0.0, b)
  b = min(1.0, b)
  
  d = b*(srv_bnd[1]-srv_bnd[0]) + srv_bnd[0]
  pwm.ChangeDutyCycle(d)
  

pwm.stop()
gpio.cleanup()

spnav_close()

