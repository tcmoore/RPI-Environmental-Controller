# Raspberry Pi Grove 2 Channel SPDT Relay Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	D4 	    D4 & D5 	    DIGITAL 		Grove - 2-Channel SPDT Switch 1 (Top Connector) – LED Lights
#							                      Grove - 2-Channel SPDT Switch 1 (Bottom Connector) – Exhaust Fan

import grovepi

def main()
  light = 4
	grovepi.pinMode(light,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital pin D4 on port D4
	grovepi.digitalWrite(light,1)   # turn on light
  time.sleep(3)                   # for 3 sec
  grovepi.digitalWrite(light,0)   # turn off light
   
	fan = 5
	grovepi.pinMode(fan,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
  grovepi.digitalWrite(fan,1)     # turn on exhaust fan
  time.sleep(3)                   # for 3 sec
  grovepi.digitalWrite(fan,0)     # turn off exhaust fan
 
  # run main() function
if __name__ == "__main__":
    main()
