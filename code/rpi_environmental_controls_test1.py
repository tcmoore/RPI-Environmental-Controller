# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 12.22.18

# code that measures temp, humidity, & soil moisture, sets alarms, saves alarm data, increases humidity in growbox,
# & displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

#!/usr/bin/env python
# coding=utf-8

# RPI/Grove Pinout Definitions
# Port# 	Pin on Port# 	Type			Sensor/Module
# ---------------------------------------------------------------
# SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer
# D2 	D2			DIGITAL 			Grove - Temperature&Humidity Sensor Pro
# D3 	D3			DIGITAL 			Grove - Water Atomization
# D4 	D4 & D5 	DIGITAL				Grove - 2-Channel SPDT Switch 1 (Bottom Connector) - Exhaust Fan
#                              			Grove 2-Channel SPDT Switch 1 (Bottom Connector) Exhaust Fan
# D5 	D5 & D6 	DIGITAL 			-
# D6 	D6	 		DIGITAL 			Temp Alarm LED
# D7 	D7	 		DIGITAL 			Humid Alarm LED
# D8 	D8	 		DIGITAL 			Moisture Alarm LED
# A0 	A0 & A1 	ANALOG 				-
# A1 	A1	 		ANALOG				Grove MQ2 Air Sensor
# A2	A2 			ANALOG 				Grove - Moisture Sensor
# I2C-1 			I2C 				-
# I2C-2 			I2C 				-
# I2C-3 			I2C 				Grove - LCD RGB Backlight
# RPRISER 			RPI SERIAL

import datetime
#import grovepi
#import setup_rpi
#import get
import check_alarms
#import control
#import send_values
#import grove_rgb_lcd

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
# LIGHT_START = 5:00	# turn on light @ 5AM
# LIGHT_STOP = 17:00	# turn off light @ 5PM

temp = 75
temp_alarm = "YES"
humidity = 75
humid_alarm = "YES"
moisture = 400
moisture_alarm = "YES"
density = 800
smoke_alarm = "YES"
fan_on = "YES"
atomizer_on = "YES"

# --------------Setup Hardware	---------------------
# setup_rpi(BUZZER, GAS_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED)

def main_code():
	print("i am from my_module.py")
	print(HI_DENSITY)
	
	while True:
		# --------------------------------------------------------------------	
		# Get current date & time
		data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
		print("Data Date/Time is ", data_time)

		# --------------------------------------------------------------------
		# check for alarms
		temp_alarm = check_alarms.check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED)
		print("Temp Alarm is ",temp_alarm)

# run main() function
if __name__ == "__main__":
	print("Executing as main program")
	print("Value of __name__ is: ", __name__)
	main_code()