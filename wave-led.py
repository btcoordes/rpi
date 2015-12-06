import RPi.GPIO as gpio
from time import sleep
import sys

pin=8

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

pwm = gpio.PWM(pin, 50)
pwm.start(0)

import math

period=2 # wave period in seconds
dt=0.02
theta=0
while True:
  sleep(dt)
  theta+=(2*math.pi)/(period/dt)
  if theta > 2*math.pi: theta=0
  b=max(0, math.sin(theta) + 1) / 2.0
  pwm.ChangeDutyCycle(b*100)
  #print("%0.2f" % b)
  
sleep(1)



pwm.stop()
gpio.cleanup()

