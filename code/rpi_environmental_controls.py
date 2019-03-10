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
#	SERIAL		D0			DIGITAL & SERIAL	Grove Buzzer
#	D2 			D2	 		DIGITAL 			Grove - Temperature&Humidity Sensor Pro
#	D3 			D3	 		DIGITAL 			Grove - Water Atomization
#	D4 			D4 & D5	 	DIGITAL 			Grove - 2-Channel SPDT Switch 1, Top Connector,LED Lights
#												Grove - 2-Channel SPDT Switch 1, Bottom Connector, Exhaust Fan
#	D5 			D5 & D6 	DIGITAL 			-
#	D6 			D6	 		DIGITAL 			Temp Alarm LED
#	D7 			D7	 		DIGITAL 			Humid Alarm LED
#	D8 			D8	 		DIGITAL 			Moisture Alarm LED
#	A0 	A		0 & A1 		ANALOG 				-
#	A1 			A1	 		ANALOG				Grove MQ2 Air Sensor
#	A2			A2 			ANALOG 				Grove - Moisture Sensor
#	I2C-1 		I2C 			-
#	I2C-2 		I2C 			-
#	I2C-3 		I2C 							Grove - LCD RGB Backlight
#	RPRISER 	RPI SERIAL

#!/usr/bin/env python
import datetime
import time
import setup_rpi
import get
import check_alarms
import control
import send_values

# --------------Setup Constants	---------------------
# Hardware constants
BUZZER = 0
GAS_SENSOR = 1
TEMP_SENSOR = 2
ATOMIZER = 3
LIGHT = 4
FAN = 5
TEMP_ALARM_LED = 6
HUMID_ALARM_LED = 7
MOISTURE_ALARM_LED = 8

#Software constants
HI_TEMP = 80	# max allowable temp
LO_TEMP = 65	# min allowable temp
HI_HUMID = 85	# max allowable humidity percentage
LO_HUMID = 65	# min allowable humidity percentage
HI_MOISTURE = 700	# max allowable soil moisture level
LO_MOISTURE = 300	# min allowable soil moisture level
HI_DENSITY = 1000	# max allowable air density
FAN_HI_TEMP = 80	# max allowable temp
FAN_LO_TEMP = 65	# min allowable temp
FAN_HI_HUMID = 85	# max allowable humidity percentage
FAN_LO_HUMID = 65	# min allowable humidity percentage
FAN_HI_MOISTURE = 700	# max allowable soil moisture level	
ATOMIZER_LO_HUMIDITY = 65	# humidity level water atomizer turns on
LIGHT_START = '5:00'	# turn on light @ 5AM
LIGHT_STOP = '17:00'	# turn off light @ 5PM

# Setup Hardware
setup_rpi.hardware(BUZZER, GAS_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED)

while True:
	# --------------------------------------------------------------------
	# Get current date & time
	data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
	print("Data Date/Time is ", data_time)

	light_time = datetime.datetime.now().strftime("%H:%M")	# Only need hours:minutes
	print("Light Date/Time is ", light_time)

	# --------------------------------------------------------------------
	# Get sesor data...
	# Get Temperature & Humidity
	# Fahrenheit = 9.0/5.0 * Celsius + 32
	temp, humidity = get.temp()
	print("Temp is: ", temp," F - Humidity is: ",humidity,"%")
			
	# Get Soil Moisture & check if there is an alarm
	#   Here are suggested sensor values:
	#       Min  Typ  Max  Condition
	#       0    0    0    sensor in open air
	#       0    20   300  sensor in dry soil
	#       300  580  700  sensor in humid soil
	#       700  940  950  sensor in water
	moisture = get.moisture()
	print("Moisture =", moisture)
					
	# Get Air Quality Value from MQ2 sensor
	density = get.air(GAS_SENSOR)
	print("Density =", density)
        		
	# --------------------------------------------------------------------
	# check for alarms
	temp_alarm = check_alarms.check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED)
	humid_alarm = check_alarms.check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED)
	moisture_alarm = check_alarms.check_moisture(LO_MOISTURE, HI_MOISTURE, moisture, MOISTURE_ALARM_LED)
	smoke_alarm = check_alarms.check_gas(HI_DENSITY, density, BUZZER)
			
	# --------------------------------------------------------------------
	# Turn Fan on if temperature is too high or humidity is too high
	fan_on = control.fan(temp, humidity, FAN_HI_TEMP, FAN_LO_TEMP, FAN_HI_HUMID, FAN_LO_HUMID, FAN)
			
	# turn on water atomizer if humidity is too low
	atomizer_on = control.atomizer(humidity, ATOMIZER)
			
	# turn on/off lights based on a certain time
	light_on = control.light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)
			
	# --------------------------------------------------------------------
	# Print values to std out console
	send_values.print_to_stdio(data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
		moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm,
		fan_on, atomizer_on)
			
	# --------------------------------------------------------------------
	# Append values to a file
	send_values.save_to_file(data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
		moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm,
		fan_on, atomizer_on)

	# --------------------------------------------------------------------
	# Display Environmental Data on LCD Screen
	send_values.print_to_LCD(data_time, temp, temp_alarm, humidity, humid_alarm, moisture, moisture_alarm, density,
		smoke_alarm, fan_on, atomizer_on)
			
	time.sleep(300)	# wait for 5 minutes before taking another set of data
