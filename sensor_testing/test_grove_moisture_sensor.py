# Raspberry Pi Grove Moisture Sensor Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer

import grovepi
import grovepi_plus_get_soil_moisture

def main():

      # --------------------------------------------------------------------
			# Get Soil Moisture & check if there is an alarm
			#   Here are suggested sensor values:
			#       Min  Typ  Max  Condition
			#       0    0    0    sensor in open air
			#       0    20   300  sensor in dry soil
			#       300  580  700  sensor in humid soil
			#       700  940  950  sensor in water
      
			# ****** MAKE SURE TO CHANGE THE PORT # IN grovepi_plus_get_soil_moisture.py *****
      moisture = grovepi_plus_get_soil_moisture.moisture
      print(moisture)
      
  # run main() function
if __name__ == "__main__":
    main()
