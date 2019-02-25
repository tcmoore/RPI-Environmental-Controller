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
import grovepi
import grovepi_plus_get_temp_humidity
import grovepi_plus_get_soil_moisture
import grovepi_plus_gas_sensor_mq2

def main()
	# define the main() function
	# ...
	# Initialize alarm flags
	temp_alarm = False
	humid_alarm = False
	moisture_alarm = False
	smoke_alarm = False
	
	# --------------Setup Hardware	---------------------
	buzzer = 0
	grovepi.pinMode(buzzer,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
	
	temp_alarm_led = 6
	grovepi.pinMode(temp_alarm_led,"OUTPUT")  # Connect Temperature Alarm LED to digital port D6

	humid_alarm_led = 7
	grovepi.pinMode(humid_alarm_led,"OUTPUT") # Connect Humidity Alarm LED to digital port D7
	
	moisture_alarm_led = 8
	grovepi.pinMode(moisture_alarm_led,"OUTPUT") # Connect Moisture Alarm LED to digital port D8
		
	light = 4
	grovepi.pinMode(light,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital pin D4 on port D4
	
	fan = 5
	grovepi.pinMode(fan,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
	
	gas_sensor = 1
	grovepi.pinMode(gas_sensor,"INPUT") # Connect the Grove Gas Sensor to analog port A1
	
	time.sleep(1)
	
	# --------------------------------------------------------------------
	# Get Nominal Air Quality Value from MQ2 sensor
	# Get sensor value
        nominal_sensor_value = grovepi.analogRead(gas_sensor)

        # Calculate gas density - large value means more dense gas
        nominal_density = (float)(nominal_sensor_value / 1024.0)

        print("nominal_sensor_value =", nominal_sensor_value, " nominal_density =", nominal_density)
        time.sleep(.5)

	
	while True:
		try:
			# --------------------------------------------------------------------	
			# Get current date & time
			now = current_date_time.now
	
			# --------------------------------------------------------------------
			# Get Temperature & Humidity
			temp = grovepi_plus_get_temp_humidity.temp
			humidity = grovepi_plus_get_temp_humidity.humidity
			
			# check for temp alarm
			if temp < 18 or temp > 25:
				temp_alarm = True
				# turn on temp alarm led
		 		grovepi.digitalWrite(temp_alarm_led,1)     # Send HIGH to switch on LED		
			else:
				temp_alarm = False
				# turn off temp alarm led
		 		grovepi.digitalWrite(temp_alarm_led,0)     # Send LOW to switch off LED		
					
			# check for humidity alarm
			if humidity < 40 or humidity > 80:
				humid_alarm = True
		 		grovepi.digitalWrite(humid_alarm_led,1)     # Send HIGH to switch on LED		
			else:
				humid_alarm = False
		 		grovepi.digitalWrite(humid_alarm_led,0)     # Send LOW to switch off LED		
	
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
				moisture_alarm = True
				grovepi.digitalWrite(moisture_alarm_led,1)     # Send HIGH to switch on LED		
			else:
				moisture_alarm = False
				grovepi.digitalWrite(moisture_alarm_led,0)     # Send LOW to switch off LED		
				
			# --------------------------------------------------------------------
			# Get Air Quality Value from MQ2 sensor
			# Get sensor value
        		sensor_value = grovepi.analogRead(gas_sensor)
        		# Calculate gas density - large value means more dense gas
        		density = (float)(sensor_value / 1024.0)
        		print("sensor_value =", sensor_value, " density =", density)
        		time.sleep(.5)
	
			# Still need to figure out alarm code 
	
	
	
# run main() function
if __name__ == "__main__":
    main()


