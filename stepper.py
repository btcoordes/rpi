import RPi.GPIO as gpio
from time import sleep


gpio.setmode(gpio.BOARD)

pdir = 10
pstep = 8

gpio.setup(pdir, gpio.OUT)
gpio.setup(pstep, gpio.OUT)

def step(dt):
  gpio.output(pstep, True)
  sleep(dt)
  gpio.output(pstep, False)
  sleep(dt)


def run(direction=True, dt=0.01, numsteps=10000000):
  gpio.output(pdir, direction)
  for i in range(numsteps):
    step(dt)


