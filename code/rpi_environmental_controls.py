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

#!/usr/bin/env python
import datetime
import grovepi
import grovepi_plus_get_temp_humidity
import grovepi_plus_get_soil_moisture
import grove_rgb_lcd

def main()
	# define the main() function
	# ...
	# Constants
	LO_TEMP = 67
	HI_TEMP = 76
	LO_HUMID = 62
	HI_HUMID = 80
	LO_MOISTURE = 300
	HI_MOISTURE = 700
	

	str temp_alarm = "OFF"
	str humid_alarm = "OFF"
	str moisture_alarm = "OFF"
	str smoke_alarm = "OFF"
	str fan_on = "OFF"
	str atomizer_on = "OFF"
	
	# --------------Setup Hardware	---------------------
	light = 4
	grovepi.pinMode(light,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital pin D4 on port D4
	
	
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
			now = datetime.datetime.now()
		 	print("Date/Time is ", now.strftime("%Y-%m-%d %I:%M"))

			# --------------------------------------------------------------------
			# Get Temperature & Humidity
			# Fahrenheit = 9.0/5.0 * Celsius + 32
			temp = (9.0/5.0 * grovepi_plus_get_temp_humidity.temp) + 32))
			humidity = grovepi_plus_get_temp_humidity.humidity
			moisture = grovepi_plus_get_soil_moisture.moisture
			print("Temp is: ", temp," F - Humidity is: ",humidity,"% Moisture is: ", moisture)
			
			# --------------------------------------------------------------------
			# check for alarms
			temp_alarm = check_alarms.temp_alarm
			humid_alarm = check_alarms.humid_alarm
			moisture_alarm = check_alarms.moisture_alarm

			# --------------------------------------------------------------------
			# Get Air Quality Value from MQ2 sensor
			# Get sensor value
        		sensor_value = grovepi.analogRead(gas_sensor)
        		# Calculate gas density - large value means more dense gas
        		density = (float)(sensor_value / 1024.0)
        		print("sensor_value =", sensor_value, " density =", density)
        		time.sleep(.5)
	
			# Still need to figure out alarm code 
		
			# --------------------------------------------------------------------
			# Turn Fan on if temperature is too high or humidity is too high
			if temp > 77 or humidity > 80:
				fan_on = "ON"
				grovepi.digitalWrite(fan,1)     # turn on exhaust fan	
			else:
				fan_on = "OFF"
				grovepi.digitalWrite(fan,0)     # turn off exhaust fan		
			print("Fan is ",fan_on)
			
			# --------------------------------------------------------------------
			# turn on water atomizer if humidity is too low
			if humidity < 40:
				atomizer_on = "ON"
		 		grovepi.digitalWrite(atomizer,1)     # turn on humidity alarm led		
			else:
				atomizer_on = "OFF"
		 		grovepi.digitalWrite(atomizer,0)     # turn off humidity alarm led		
			print("Atomizer is ", atomizer_on)
			
			# --------------------------------------------------------------------
			# Display Environmental Data on LCD Screen
			setRGB(0,128,64)
    			time.sleep(2)
			setText("Date/Time: ", now.strftime("%Y-%m-%d %I:%M"))
    			time.sleep(5)
			setText("Temp:",str(temp)," F - Alarm:",temp_alarm)
    			time.sleep(5)
			setText("Humidity:",str(humidity),"% - Alarm:",humidity_alarm,"Atomizer is ",atomizer_on) 
    			time.sleep(5)		
			setText("Moisture: ", str(moisture)," - Alarm:",moisture_alarm)
    			time.sleep(5)
			setText("Fan is ",fan_on)
    			time.sleep(5)
			setText("Nominal Air Sensor=",nominal_sensor_value," Nominal Density=",nominal_density)
			time.sleep(5)
			setText("Current Air Sensor=",sensor_value," density=",density)
			time.sleep(5)	
			
# run main() function
if __name__ == "__main__":
    main()
