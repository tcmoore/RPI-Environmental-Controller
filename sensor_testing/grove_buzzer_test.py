# Raspberry Pi Grove Buzzer Testing
# Todd Moore
# 3.5.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer

import GrovePi
import time

# def main()

# --------------Setup Hardware	---------------------
buzzer = 0
grovepi.pinMode(buzzer,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
time.sleep(.5)

density = 100
HI_DENSITY = 50 
  
# check for smoke alarm
if density > HI_DENSITY:
	moke_alarm = "ON"
	grovepi.digitalWrite(buzzer,1)     # Turn on buzzer		
else:
	smoke_alarm = "OFF"
	grovepi.digitalWrite(buzzer,0)     # Turn off buzzer
print("Smoke Alarm is ",smoke_alarm)

#   # run main() function
# if __name__ == "__main__":
#     main()
