# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 12.22.18

# code that measures temp, humidity, & soil moisture, sets alarms, saves alarm data, increases humidity in growbox,
# & displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer
#	D2 	D2	 	DIGITAL 		Grove - Temperature&Humidity Sensor Pro
#	D3 	D3	 	DIGITAL 		Grove - Water Atomization
#	D4 	D4 & D5 	DIGITAL 		Grove - 2-Channel SPDT Switch 1 (Top Connector) – LED Lights
#							Grove - 2-Channel SPDT Switch 1 (Bottom Connector) – Exhaust Fan
#	D5 	D5 & D6 	DIGITAL 		-
#	D6 	D6	 	DIGITAL 		Temp Alarm LED
#	D7 	D7	 	DIGITAL 		Humid Alarm LED
#	D8 	D8	 	DIGITAL 		Moisture Alarm LED
#	A0 	A0 & A1 	ANALOG 			-
#	A1 	A1	 	ANALOG			Grove MQ2 Air Sensor
#	A2	A2 		ANALOG 			Grove - Moisture Sensor
#	I2C-1 			I2C 			-
#	I2C-2 			I2C 			-
#	I2C-3 			I2C 			Grove - LCD RGB Backlight
#	RPRISER 		RPI SERIAL

import current_date_time
import grovepi_plus_get_temp_humidity
import grovepi_plus_get_soil_moisture
import grovepi_plus_gas_sensor_mq2
import check_alarms

def main()
	# define the main() function
	# ...
	# Initialize alarm flags
	temp_alarm = "NO"
	humid_alarm = "NO"
	moisture_alarm = "NO"
	smoke_alarm = "NO"
	
	while True:
		try:
			# --------------------------------------------------------------------	
			# Get current date & time
			now = current_date_time.now
			# --------------------------------------------------------------------
	
			# --------------------------------------------------------------------
			# Get Temperature & Humidity
			temp = grovepi_plus_get_temp_humidity.temp
			humidity = grovepi_plus_get_temp_humidity.humidity
			
			# check for temp alarm
			if temp < 18 or temp > 25:
				temp_alarm = "YES!"
				# turn on temp alarm led
				
			else:
				temp_alarm = "NO"
				
			# check for humidity alarm
			if humidity < 40 or humidity > 80:
				humid_alarm = "YES!"
			else:
				humid_alarm = "NO"
			# --------------------------------------------------------------------
	
			# --------------------------------------------------------------------
			# Get Soil Moisture & check if there is an alarm
			#   Here are suggested sensor values:
			#       Min  Typ  Max  Condition
			#       0    0    0    sensor in open air
			#       0    20   300  sensor in dry soil
			#       300  580  700  sensor in humid soil
			#       700  940  950  sensor in water
			moisture = grovepi_plus_get_soil_moisture.moisture
			
			# check for soil moisture alarm
			if moisture < 200 or moisture > 800:
				moisture_alarm = "YES!"
			else:
				moisture_alarm = "NO"
			# --------------------------------------------------------------------
	
			# --------------------------------------------------------------------
			# Get Air Quality Value from MQ2 sensor & check for an alarm
			sensor_value = grovepi_plus_gas_sensor_mq2.sensor_value
			density = grovepi_plus_gas_sensor_mq2.density
			# --------------------------------------------------------------------
			
			# --------------------------------------------------------------------
			
		
	
	
	
	
# run main() function
if __name__ == "__main__":
    main()


