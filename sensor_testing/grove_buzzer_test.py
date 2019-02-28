# Raspberry Pi Grove Buzzer Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer

import grovepi

def main()

# --------------Setup Hardware	---------------------
	buzzer = 0
	grovepi.pinMode(buzzer,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
  
  time.sleep(1)

  grovepi.digitalWrite(buzzer,1)    # turn on buzzer
  time.sleep(3)                     # keep buzzer on for 3 sec
  grovepi.digitalWrite(buzzer,0)    # turn off buzzer
  
  # run main() function
if __name__ == "__main__":
    main()
