# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 3.12.19

# code that measures temp, humidity, & soil moisture (for 2 plants), sets alarms, saves alarm data, increases humidity in growbox,
# & displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions

#	Port #	Pins on Port #	Type				Sensor Pin	Sensor/Module
#	-----------------------------------------------------------------------------------------
#	SERIAL	D0 & D1			DIGITAL & SERIAL	D0			Grove - 2-Channel SPDT Switch 1 (Top 
# 																	Connector) – LED Lights
#												D1			Grove - 2-Channel SPDT Switch 1 (Bottom
# 																	 Connector) – Exhaust Fan
# 	D2		D2 & D3			DIGITAL				D2			Grove Buzzer
#	D3		D3 & D4			DIGITAL				D3			Temp Alarm LED
#												D4			Humid Alarm LED
#	D4		D4 & D5			DIGITAL				n/a
#	D5		D5 & D6			DIGITAL				D5			Smoke Alarm LED
# 	D6		D6 & D7			DIGITAL				D6			Grove - Temperature&Humidity Sensor Pro
#	D7		D7 & D8			DIGITAL				D7			Grove - Water Atomization
#	D8		D8 & D9			DIGITAL				D8			Moisture Alarm LED
#												D9			Water Atomizer LED
#					
#	A0		A0 & A1			ANALOG				A0			Grove - Moisture Sensor1
#	A1		A1 & A2			ANALOG				A1			Grove - Moisture Sensor2
#	A2		A2 & A3			ANALOG				A2			Grove MQ2 Air Sensor
#
# 	I2C-1	I2C												Free
#	I2C-2	I2C												Free
#	I2C-3	I2C												Grove - LCD RGB Backlight
#	RPRISER					RPI SERIAL			

#!/usr/bin/env python
import datetime
import time
import setup_rpi
import get
import check_alarms
import control
import send_values

# --------------Setup Constants	---------------------
# GrovePi+ Hat Digital Pin Constants
BUZZER = 0			
TEMP_SENSOR = 2
ATOMIZER = 3
LIGHT = 4
FAN = 5
TEMP_ALARM_LED = 6
HUMID_ALARM_LED = 7
MOISTURE_ALARM_LED = 8
ATOMIZER_ON_LED = 9

# GrovePi+ Hat Analog Pin Constants
GAS_SENSOR = 0	# Connect MQ2 to Analog port A0, pin 0
MOISTURE_SENSOR = 2

#Software constants
HI_TEMP = 80	# max allowable temp
LO_TEMP = 65	# min allowable temp
HI_HUMID = 85	# max allowable humidity percentage
LO_HUMID = 65	# min allowable humidity percentage
HI_DENSITY = 1000 # max allowable density number
FAN_HI_TEMP = 80	# max allowable temp
FAN_LO_TEMP = 65	# min allowable temp
FAN_HI_HUMID = 85	# max allowable humidity percentage
FAN_LO_HUMID = 65	# min allowable humidity percentage
FAN_HI_MOISTURE = 700	# max allowable soil moisture level	
ATOMIZER_LO_HUMIDITY = 65	# humidity level water atomizer turns on
LIGHT_START = '5:00'	# turn on light @ 5AM
LIGHT_STOP = '17:00'	# turn off light @ 5PM

# temp_humidity_sensor_type
# This represents the cover color of the sensor. I have the white type.
#BLUE = 0    # The Blue colored sensor.
WHITE = 1   # The White colored sensor.

# Setup Hardware
setup_rpi.hardware(BUZZER, GAS_SENSOR, MOISTURE_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED, ATOMIZER_ON_LED)

while True:
	# Get current date & time
	data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
	print("Data Date/Time is ", data_time)

	light_time = datetime.datetime.now().strftime("%H:%M")	# Only need hours:minutes
	print("Light Date/Time is ", light_time)

	# Get sesor data...
	# Get Temperature in F & Humidity
	tempF, humidity = get.temp(TEMP_SENSOR, WHITE)
				
	# Get Soil Moisture & check if there is an alarm
	#   Here are suggested sensor values:
	#       Min  Typ  Max  Condition
	#       0    0    0    sensor in open air
	#       0    20   300  sensor in dry soil
	#       300  580  700  sensor in humid soil
	#       700  940  950  sensor in water
	
	# 	Sensor values observer: 
	# 		Values  Condition
	#		--------------------------
	# 		0-17	sensor in open air
	# 		18-424  sensor in dry soil
	# 		425-689 sensor in humid soil
	# 		690+  	sensor in water
	moisture = get.moisture(MOISTURE_SENSOR)
					
	# Get Air Quality Value from MQ2 sensor
	density = get.air(GAS_SENSOR)
        		
	# check for alarms
	temp_alarm = check_alarms.check_temp(LO_TEMP, HI_TEMP, tempF, TEMP_ALARM_LED)
	humid_alarm = check_alarms.check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED)
	moisture_alarm = check_alarms.check_moisture(moisture, MOISTURE_ALARM_LED)
	smoke_alarm = check_alarms.check_gas(HI_DENSITY, density, BUZZER)
			
	# Turn Fan on if temperature is too high or humidity is too high
	fan_on = control.fan(tempF, humidity, FAN_HI_TEMP, FAN_LO_TEMP, FAN_HI_HUMID, FAN_LO_HUMID, FAN)
			
	# turn on water atomizer if humidity is too low
	atomizer_on = control.atomizer(humidity, ATOMIZER)
			
	# turn on/off lights based on a certain time
	light_on = control.light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)

	# Append values to a file
	send_values.save_to_file(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
				moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on)

	# Print values to std out console
	send_values.print_to_stdio(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
				moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on)

	# Display Environmental Data on LCD Screen
	send_values.print_to_LCD(data_time, tempF, temp_alarm, humidity, humid_alarm, moisture, moisture_alarm, density,
		smoke_alarm, fan_on, atomizer_on)
			
	time.sleep(300)	# wait for 5 minutes before taking another set of data
