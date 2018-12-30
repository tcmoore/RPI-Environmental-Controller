# Raspberry Pi Code to respond to a switch being pressed
# Switch is connected to GPIO 17 pin. Once pressed pin will be
# connected to ground.

import time
import PRi.GPIO as io

# setup GPIO 17 as input, w/ pull-up activated
switch_pin = 17
io.setmode(io.BCM)
io.setup(switch_pin, io.IN, pull_up_down=io.PUD_UP)

while True:
  h = time.localtime().tm_hour
  m = time.localtime().tm_min
  key_pressed = not io.input(switch_pin)
  if key pressed:
    print(h, " ", m)
    
