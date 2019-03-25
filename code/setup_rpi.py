# setup_rpi
# Todd Moore
# 3.9.19

# sets up the RPI & GrovePi+ Hat hardware inputs & outputs

import time
import grovepi
import config

def hardware():
    
    # setup RPI/GrovePi+ hardware pins
    # --------------Setup Hardware  ---------------------
    grovepi.pinMode(config.BUZZER,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital output
    time.sleep(.5)
        
    grovepi.pinMode(config.GAS_SENSOR,"INPUT") # Connect the Grove Gas Sensor to analog input
    time.sleep(.5)
    
    grovepi.pinMode(config.MOISTURE_SENSOR,"INPUT") # Connect the Grove Moisture Sensor to analog input
    time.sleep(.5)

    grovepi.pinMode(config.TEMP_SENSOR,"INPUT") # Connect the Grove Temp/Humid Sensor to digital input
    time.sleep(.5)

    grovepi.pinMode(config.ATOMIZER,"OUTPUT") # Connect the Grove Water Atomizer to digital output
    time.sleep(.5)

    grovepi.pinMode(config.LIGHT,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital output
    time.sleep(.5)
    
    grovepi.pinMode(config.FAN,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital output
    time.sleep(.5)
    
    grovepi.pinMode(config.TEMP_ALARM_LED,"OUTPUT")  # Connect Temperature Alarm LED to digital output
    time.sleep(.5)      
        
    grovepi.pinMode(config.HUMID_ALARM_LED,"OUTPUT") # Connect Humidity Alarm LED to digital output
    time.sleep(.5)
        
    grovepi.pinMode(config.MOISTURE_ALARM_LED,"OUTPUT") # Connect Moisture Alarm LED to digital output
    time.sleep(.5)

    grovepi.pinMode(config.ATOMIZER_ON_LED,"OUTPUT") # Connect Atomizer ON LED to digital output
    time.sleep(.5)
    