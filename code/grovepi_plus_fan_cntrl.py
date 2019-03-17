# Turn on/off exhaust fan using top relay of Grove 2 channel relay connected to GrovePi+ to digital pin D5 on port D4
# http://wiki.seeedstudio.com/Grove-2-Channel_SPDT_Relay/

import time
# import grovepi
from grovepi import *

# Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
# SIG,NC,VCC,GND
fan = 0

pinMode(fan,"OUTPUT")

while True:
    try:
        # Turn fan on for 10 seconds
        digitalWrite(fan,1)
        print ('start')
        time.sleep(5)

        # Turn off fan for 10 seconds and repeat
        digitalWrite(fan,0)
        print ('stop')
        time.sleep(5)

    except KeyboardInterrupt:
        digitalWrite(fan,0)
        break
    except IOError:
        print ("Error")
