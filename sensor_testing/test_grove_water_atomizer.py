# Raspberry Pi Grove Water Atomizer Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	D3 	          D3	 	  DIGITAL 		Grove - Water Atomization

import grovepi

def main()

# --------------Setup Hardware	---------------------
	atomizer = 3
	grovepi.pinMode(atomizer,"OUTPUT") # Connect the Grove water atomizer to digital pin D3 on port D3
	time.sleep(1)

  grovepi.digitalWrite(atomizer,1)    # turn on buzzer
  time.sleep(3)                       # keep water atomizer on for 3 sec
  grovepi.digitalWrite(atomizer,0)    # turn off buzzer
  
  # run main() function
if __name__ == "__main__":
    main()
