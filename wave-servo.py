import RPi.GPIO as gpio
from time import sleep
import sys

pin=8

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

pwm = gpio.PWM(pin, 50)
pwm.start(0)

import math

srv_bnd=[float(sys.argv[1]),float(sys.argv[2])]

period=3 # wave period in seconds
dt=0.05
theta=0
while True:
  sleep(dt)
  theta+=(2*math.pi)/(period/dt)
  if theta > 2*math.pi: theta=0
  b=max(0, math.sin(theta) + 1) / 2.0
  b = b*(srv_bnd[1]-srv_bnd[0]) + srv_bnd[0]
  pwm.ChangeDutyCycle(b)
  #print("%0.2f" % b)
  
sleep(1)



pwm.stop()
gpio.cleanup()

