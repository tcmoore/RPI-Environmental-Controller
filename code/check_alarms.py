# check_alarms.py
# Todd Moore
# 3.9.19

# code that checks temp, humidity, soil moisture, & sets alarms if too high or too low.
# also checks Gas Density & sets smoke alarm if too high.

#!/usr/bin/env python
# coding=utf-8

import datetime
# import grovepi

def check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED):
	# --------------------------------------------------------------------
	# check for temp alarm
	if HI_TEMP > temp > LO_TEMP:
		temp_alarm = "OFF"
	# 	# grovepi.digitalWrite(TEMP_ALARM_LED, 0)     # turn off temp alarm led	
	else:
		temp_alarm = "ON"
	# 	# grovepi.digitalWrite(TEMP_ALARM_LED, 1)     # turn on temp alarm led		
	print("Temp Alarm is ",temp_alarm)
	print("check_temp done")
	return temp_alarm
	
def check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED):
	# --------------------------------------------------------------------
	# check for humidity alarm
	if HI_HUMID > humidity > LO_HUMID:
		humid_alarm = "OFF"
		# grovepi.digitalWrite(HUMID_ALARM_LED, 0)     # turn off humidity alarm led		
	else:
		humid_alarm = "ON"
		# grovepi.digitalWrite(HUMID_ALARM_LED, 1)     # turn on humidity alarm led		
	print("Humid Alarm is ", humid_alarm)
	print("check_humidity done")
	return humid_alarm
		
def check_moisture(LO_MOISTURE, HI_MOISTURE, moisture, MOISTURE_ALARM_LED):
	# --------------------------------------------------------------------
	# Check if there is a soil moisture alarm
	#   Here are suggested sensor values:
	#       Min  Typ  Max  Condition
	#       0    0    0    sensor in open air
	#       0    20   300  sensor in dry soil
	#       300  580  700  sensor in humid soil
	#       700  940  950  sensor in water
		
	# check for soil moisture alarm
	if HI_MOISTURE > moisture > LO_MOISTURE:
		moisture_alarm = "OFF"
		# grovepi.digitalWrite(MOISTURE_ALARM_LED, 0)     # Turn off soil moisture alarm led		
	else:
		moisture_alarm = "ON"
		# grovepi.digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on soil moisture alarm led
	print("Moisture Alarm is ",moisture_alarm)
	print("check_moisture done")
	return moisture_alarm
		
def check_gas(HI_DENSITY, density, BUZZER):
	# check for smoke alarm
	if density < HI_DENSITY:
		smoke_alarm = "OFF"
		# grovepi.digitalWrite(BUZZER, 0)     # Turn off buzzer		
	else:
		smoke_alarm = "ON"
		# grovepi.digitalWrite(BUZZER, 1)     # Turn on buzzer
	print("Smoke Alarm is ",smoke_alarm)
	print("check_gas done")
	return smoke_alarm

# run main() function
if __name__ == "__main__":
	print("Executing as main program")
	print("Value of __name__ is: ", __name__)
	# -------- Test Vectors ------------
	# Hardware constants
	BUZZER = 0
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
	temp = 78
	humidity = 90
	moisture = 800
	density = 1100
	print("High Temp, Low Temp, & Temp Vectors are: ", HI_TEMP, LO_TEMP, temp)
	check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED)
	print("High Humid, Low Humid, & Humidity Vectors are: ", HI_HUMID, LO_HUMID, humidity)
	check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED)
	print("High Moisture, Low Moisture, & Moisture Vectors are: ", HI_MOISTURE, LO_MOISTURE, moisture)
	check_moisture(LO_MOISTURE, HI_MOISTURE, moisture, MOISTURE_ALARM_LED)
	print("High Density, & Density Vectors are: ", HI_DENSITY, density)
	check_gas(HI_DENSITY, density, BUZZER)