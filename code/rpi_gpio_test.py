# GPIO LED EXAMPLE TO TEST CONTROLLING RPI GPIO
# T.MOORE
# 12.29.18

import RPi.GPIO as GPIO     ## Import GPIO library

GPIO.setmode(GPIO.BOARD)    ## Use board pin numbering
GPIO.setup(36, GPIO.OUT)    ## Setup GPIO pin 36 to OUT
GPIO.output(36, False)       ## Turn on GPIO pin 36- 
 
