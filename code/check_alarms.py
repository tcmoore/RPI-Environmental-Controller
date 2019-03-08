# check_alarms.py
# Todd Moore
# 3.8.19

# code that checks temp, humidity, and soil moisture & sets alarms if too high or too low.

#!/usr/bin/env python
# coding=utf-8

import datetime
import grovepi

# def check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED)
def check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED):
	# --------------------------------------------------------------------
	# check for temp alarm
	if LO_TEMP > temp > HI_TEMP:
		temp_alarm = "ON"
	# 	# grovepi.digitalWrite(temp_alarm_led,1)     # turn on temp alarm led	
	else:
		temp_alarm = "OFF"
	# 	# grovepi.digitalWrite(temp_alarm_led,0)     # turn off temp alarm led		
	print("Temp Alarm is ",temp_alarm)
	print("check_temp done")
	return temp_alarm
	
	
		
# def check_humidity(LO_HUMID, HI_HUMID, humidity, humid_alarm_led)
# 	# --------------------------------------------------------------------
# 	# check for humidity alarm
# 	if LO_HUMID > humidity > HI_HUMID:
# 		humid_alarm = "ON"
# 		grovepi.digitalWrite(humid_alarm_led,1)     # turn on humidity alarm led		
# 	else:
# 		humid_alarm = "OFF"
# 		grovepi.digitalWrite(humid_alarm_led,0)     # turn off humidity alarm led		
# 	print("Humid Alarm is ", humid_alarm)
# 	return humid_alarm
		
# def check_moisture(LO_MOISTURE, HI_MOISTURE, moisture, moisture_alarm_led)
# 	# --------------------------------------------------------------------
# 	# Check if there is a soil moisture alarm
# 	#   Here are suggested sensor values:
# 	#       Min  Typ  Max  Condition
# 	#       0    0    0    sensor in open air
# 	#       0    20   300  sensor in dry soil
# 	#       300  580  700  sensor in humid soil
# 	#       700  940  950  sensor in water
		
# 	# check for soil moisture alarm
# 	if lo_moisture > moisture > hi_moisture:
# 		moisture_alarm = "ON"
# 		grovepi.digitalWrite(moisture_alarm_led,1)     # Send HIGH to switch on LED		
# 	else:
# 		moisture_alarm = "OFF"
# 		grovepi.digitalWrite(moisture_alarm_led,0)     # Send LOW to switch off LED
# 	print("Moisture Alarm is ",moisture_alarm)
# 	return moisture_alarm
		
# def check_gas(HI_DENSITY, density, buzzer)
# 	# check for smoke alarm
# 	if density > HI_DENSITY:
# 		smoke_alarm = "ON"
# 		grovepi.digitalWrite(buzzer,1)     # Turn on buzzer		
# 	else:
# 		smoke_alarm = "OFF"
# 		grovepi.digitalWrite(buzzer,0)     # Turn off buzzer
# 	print("Smoke Alarm is ",smoke_alarm)
# 	return smoke_alarm