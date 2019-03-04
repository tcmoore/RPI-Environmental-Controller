check_alarms.py
Todd Moore
3.1.19

# code that checks temp, humidity, and soil moisture & sets alarms if too high or too low.

import grovepi

	def check_temp(hi_temp, lo_temp)
		temp_alarm_led = 6
		grovepi.pinMode(temp_alarm_led,"OUTPUT")  # Connect Temperature Alarm LED to digital port D6
		time.sleep(1)		
		
		# --------------------------------------------------------------------
		# check for temp alarm
		if lo_temp > temp > hi_temp:
			temp_alarm = "ON"
			grovepi.digitalWrite(temp_alarm_led,1)     # turn on temp alarm led	
		else:
			temp_alarm = "OFF"
			grovepi.digitalWrite(temp_alarm_led,0)     # turn off temp alarm led		
		print("Temp Alarm is ",temp_alarm)
		return temp_alarm
		
	def check_humidity(hi_humid, lo_humid)
		humid_alarm_led = 7
		grovepi.pinMode(humid_alarm_led,"OUTPUT") # Connect Humidity Alarm LED to digital port D7
		time.sleep(1)
		
		# --------------------------------------------------------------------
		# check for humidity alarm
		if lo_humid > humidity > hi_humid:
			humid_alarm = "ON"
			grovepi.digitalWrite(humid_alarm_led,1)     # turn on humidity alarm led		
		else:
			humid_alarm = "OFF"
			grovepi.digitalWrite(humid_alarm_led,0)     # turn off humidity alarm led		
		print("Humid Alarm is ", humid_alarm)
		return humid_alarm
		
	def check_moisture(hi_moisture, lo_moisture)
		moisture_alarm_led = 8
		grovepi.pinMode(moisture_alarm_led,"OUTPUT") # Connect Moisture Alarm LED to digital port D8
		time.sleep(1)
		
		# --------------------------------------------------------------------
		# Check if there is a soil moisture alarm
		#   Here are suggested sensor values:
		#       Min  Typ  Max  Condition
		#       0    0    0    sensor in open air
		#       0    20   300  sensor in dry soil
		#       300  580  700  sensor in humid soil
		#       700  940  950  sensor in water
			
		# check for soil moisture alarm
		if lo_moisture > moisture > hi_moisture:
			moisture_alarm = "ON"
			grovepi.digitalWrite(moisture_alarm_led,1)     # Send HIGH to switch on LED		
		else:
			moisture_alarm = "OFF"
			grovepi.digitalWrite(moisture_alarm_led,0)     # Send LOW to switch off LED
		print("Moisture Alarm is ",moisture_alarm)
		return moisture_alarm
		
	def check_air(hi_moisture, lo_moisture)
		gas_sensor = 1
		grovepi.pinMode(gas_sensor,"INPUT") # Connect the Grove Gas Sensor to analog port A1
		time.sleep(1)
		
		
		
def check_alarms(temp, humidity, moisture)

	# --------------Setup Hardware	---------------------
	buzzer = 0
	grovepi.pinMode(buzzer,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
	
	
	atomizer = 3
	grovepi.pinMode(atomizer,"OUTPUT") # Connect the Grove water atomizer to digital pin D3 on port D3
	
	fan = 5
	grovepi.pinMode(fan,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
	

	
	
	

	# Temp Constants
	int HI_TEMP = 77
	int LO_TEMP = 67

	# Humidity Constants
	int HI_HUMID = 80
	int LO_HUMID = 40
	
	# Soil Moisture Constants
	int HI_MOISTURE = 800
	int LO_MOISTURE = 400

	# Alarm flags
	bool moisture_alarm = "OFF"

	
