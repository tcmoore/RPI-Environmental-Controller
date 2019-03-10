# Raspberry Pi Grove Temp & Humidity Sensor Pro Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer

import grovepi
import grovepi_plus_get_temp_humidity

def main():

      # --------------------------------------------------------------------
			# Get Temperature & Humidity
			# Fahrenheit = 9.0/5.0 * Celsius + 32
			temp = 9.0/5.0 * (grovepi_plus_get_temp_humidity.temp) + 32
			humidity = grovepi_plus_get_temp_humidity.humidity
			print("Temp is: ", temp," F - Humidity is: ",humidity,"%")
      
# run main() function
if __name__ == "__main__":
    main()
