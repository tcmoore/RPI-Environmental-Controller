# setup_rpi
# Todd Moore
# 3.9.19

# sets up the RPI & GrovePi+ Hat hardware inputs & outputs

import time
import grovepi

def hardware(BUZZER, GAS_SENSOR, MOISTURE_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, 
	TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED, ATOMIZER_ON_LED):
    
    # setup RPI/GrovePi+ hardware pins
    # --------------Setup Hardware	---------------------
	grovepi.pinMode(BUZZER,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital output
	time.sleep(.5)
		
	grovepi.pinMode(GAS_SENSOR,"INPUT") # Connect the Grove Gas Sensor to analog input
	time.sleep(.5)
	
	grovepi.pinMode(MOISTURE_SENSOR,"INPUT") # Connect the Grove Moisture Sensor to analog input
	time.sleep(.5)

	grovepi.pinMode(TEMP_SENSOR,"INPUT") # Connect the Grove Temp/Humid Sensor to digital input
	time.sleep(.5)

	grovepi.pinMode(ATOMIZER,"OUTPUT") # Connect the Grove Water Atomizer to digital output
	time.sleep(.5)

	grovepi.pinMode(LIGHT,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital output
	time.sleep(.5)
	
	grovepi.pinMode(FAN,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital output
	time.sleep(.5)
	
	grovepi.pinMode(TEMP_ALARM_LED,"OUTPUT")  # Connect Temperature Alarm LED to digital output
	time.sleep(.5)		
		
	grovepi.pinMode(HUMID_ALARM_LED,"OUTPUT") # Connect Humidity Alarm LED to digital output
	time.sleep(.5)
		
	grovepi.pinMode(MOISTURE_ALARM_LED,"OUTPUT") # Connect Moisture Alarm LED to digital output
	time.sleep(.5)

	grovepi.pinMode(ATOMIZER_ON_LED,"OUTPUT") # Connect Atomizer ON LED to digital output
	time.sleep(.5)