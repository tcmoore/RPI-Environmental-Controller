main(BUZZER, GAS_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED)
    
    # setup RPI/GrovePi+ hardware pins
    # --------------Setup Hardware	---------------------
	grovepi.pinMode(BUZZER,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital port D0
	time.sleep(.5)
		
	grovepi.pinMode(GAS_SENSOR,"INPUT") # Connect the Grove Gas Sensor to analog port A1
	time.sleep(.5)
	
	grovepi.pinMode(TEMP_SENSOR,"INPUT") # Connect the Grove Temp/Humid Sensor to digital pin D2 on port D2
	time.sleep(.5)

	grovepi.pinMode(ATOMIZER,"OUTPUT") # Connect the Grove Water Atomizer to digital pin D3 on port D3
	time.sleep(.5)

	grovepi.pinMode(LIGHT,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital pin D4 on port D4
	time.sleep(.5)
	
	grovepi.pinMode(FAN,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital pin D5 on port D4
	time.sleep(.5)
	
	grovepi.pinMode(TEMP_ALARM_LED,"OUTPUT")  # Connect Temperature Alarm LED to digital port D6
	time.sleep(.5)		
		
	grovepi.pinMode(HUMID_ALARM_LED,"OUTPUT") # Connect Humidity Alarm LED to digital port D7
	time.sleep(.5)
		
	grovepi.pinMode(MOISTURE_ALARM_LED,"OUTPUT") # Connect Moisture Alarm LED to digital port D8
	time.sleep(.5)