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
import current_date_time
import grovepi
import grove_rgb_lcd

def main()
	# define the main() function
	# ...
	# Initialize alarm flags
	str temp_alarm = "OFF"
	str humid_alarm = "OFF"
	str moisture_alarm = "OFF"
	str smoke_alarm = "OFF"
	str fan_on = "OFF"
	str atomizer_on = "OFF"
	
	# --------------Setup Hardware	---------------------
	buzzer = 0
	grovepi.pinMode(buzzer,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
	
	gas_sensor = 1
	grovepi.pinMode(gas_sensor,"INPUT") # Connect the Grove Gas Sensor to analog port A1
	
	atomizer = 3
	grovepi.pinMode(atomizer,"OUTPUT") # Connect the Grove water atomizer to digital pin D3 on port D3
	
	light = 4
	grovepi.pinMode(light,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital pin D4 on port D4
	
	fan = 5
	grovepi.pinMode(fan,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
	
	temp_alarm_led = 6
	grovepi.pinMode(temp_alarm_led,"OUTPUT")  # Connect Temperature Alarm LED to digital port D6

	humid_alarm_led = 7
	grovepi.pinMode(humid_alarm_led,"OUTPUT") # Connect Humidity Alarm LED to digital port D7
	
	moisture_alarm_led = 8
	grovepi.pinMode(moisture_alarm_led,"OUTPUT") # Connect Moisture Alarm LED to digital port D8
	
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
		 	print("Date/Time is ", now.strftime("%Y-%m-%d %I:%M"))

			# --------------------------------------------------------------------
			# Get Temperature & Humidity
			# Fahrenheit = 9.0/5.0 * Celsius + 32
			temp = (9.0/5.0 * grovepi_plus_get_temp_humidity.temp) + 32))
			humidity = grovepi_plus_get_temp_humidity.humidity
			print("Temp is: ", temp," F - Humidity is: ",humidity,"%")
			
			# --------------------------------------------------------------------
			# check for temp alarm
			if temp < 67 or temp > 77:
				temp_alarm = "ON"
				grovepi.digitalWrite(temp_alarm_led,1)     # turn on temp alarm led	
			else:
				temp_alarm = "OFF"
				grovepi.digitalWrite(temp_alarm_led,0)     # turn off temp alarm led		
			print("Temp Alarm is ",temp_alarm)
			
			# --------------------------------------------------------------------
			# check for humidity alarm
			if humidity < 40 or humidity > 80:
				humid_alarm = "ON"
		 		grovepi.digitalWrite(humid_alarm_led,1)     # turn on humidity alarm led		
			else:
				humid_alarm = "OFF"
		 		grovepi.digitalWrite(humid_alarm_led,0)     # turn off humidity alarm led		
			print("Humid Alarm is ", humid_alarm)
			
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
				moisture_alarm = "ON"
				grovepi.digitalWrite(moisture_alarm_led,1)     # Send HIGH to switch on LED		
			else:
				moisture_alarm = "OFF"
				grovepi.digitalWrite(moisture_alarm_led,0)     # Send LOW to switch off LED
			print("Moisture Alarm is ",moisture_alarm)
				
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
