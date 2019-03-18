# check_alarms.py
# Todd Moore
# 3.17.19

# ******** WORKING AS OF 3.17.19 *****
# code that checks temp, humidity, soil moisture, & sets alarms if too high or too low.
# also checks Gas Density & sets smoke alarm if too high.

#!/usr/bin/env python
# coding=utf-8
from grovepi import digitalWrite

def check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED):
    # --------------------------------------------------------------------
    # check for temp alarm
    if HI_TEMP > temp > LO_TEMP:
        temp_alarm = "OFF"
        digitalWrite(TEMP_ALARM_LED, 0)     # turn off temp alarm led 
    else:
        temp_alarm = "ON"
        digitalWrite(TEMP_ALARM_LED, 1)     # turn on temp alarm led      
    print("Temp Alarm is ", temp_alarm)
    print("check_alarms.check_temp done")
    return temp_alarm
    
def check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED):
    # --------------------------------------------------------------------
    # check for humidity alarm
    if HI_HUMID > humidity > LO_HUMID:
        humid_alarm = "OFF"
        digitalWrite(HUMID_ALARM_LED, 0)     # turn off humidity alarm led        
    else:
        humid_alarm = "ON"
        digitalWrite(HUMID_ALARM_LED, 1)     # turn on humidity alarm led     
    print("Humid Alarm is ", humid_alarm)
    print("check_alarms.check_humidity done")
    return humid_alarm
        
def check_moisture(moisture, MOISTURE_ALARM_LED):
    # --------------------------------------------------------------------
    # Check if there is a soil moisture alarm
    #   Here are suggested sensor values:
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water

    # Human Readable Sensor values: 
    # Values  Condition
    # --------------------------
    # 0-17    'AIR'
    # 18-424  'DRY'
    # 425-689 'HUMID'
    # 690+    'WATER'
    
    # convert moisture value to human readable text 
    if 17 >= moisture >= 0:
        moisture_alarm = 'AIR'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is VERY dry & needs water!
    elif 424 >= moisture >= 18:
        moisture_alarm = 'DRY'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is dry & needs water!
    elif 689 >= moisture >= 425:
        moisture_alarm = 'PERFECT'
        digitalWrite(MOISTURE_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!
    elif moisture >= 690:
        moisture_alarm = 'WATER'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is WET!!!
    else:
        moisture_alarm = 'BROKEN'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause sensor is broken!!
    print("Moisture Alarm is ",moisture_alarm)
    print("check_alarms.check_moisture done")
    return moisture_alarm
        
def check_gas(HI_DENSITY, density, BUZZER, SMOKE_ALARM_LED):
    # check for smoke alarm
    if density < HI_DENSITY:
        smoke_alarm = "OFF"
        digitalWrite(BUZZER, 0)     # Turn off buzzer       
        digitalWrite(SMOKE_ALARM_LED, 0)     # Turn off buzzer       
    else:
        smoke_alarm = "ON"
        digitalWrite(BUZZER, 1)     # Turn on buzzer
        digitalWrite(SMOKE_ALARM_LED, 0)     # Turn off buzzer       
    print("Smoke Alarm is ",smoke_alarm)
    print("check_alarms.check_gas done")
    return smoke_alarm

# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    
    # -------- Test Vectors ------------
    # Hardware constants
    BUZZER = 2   
    HUMID_ALARM_LED = 3
    TEMP_ALARM_LED = 4
    SMOKE_ALARM_LED = 8
    MOISTURE_ALARM_LED = 9

    #Software constants
    HI_TEMP = 80    # max allowable temp
    LO_TEMP = 65    # min allowable temp
    HI_HUMID = 85   # max allowable humidity percentage
    LO_HUMID = 65   # min allowable humidity percentage
    HI_DENSITY = 1000   # max allowable air density
    temp = 75
    humidity = 80
    moisture = 500
    density = 800
    temp_alarm = check_temp(LO_TEMP, HI_TEMP, temp, TEMP_ALARM_LED)
    print("High Temp, Low Temp, Temp, & Temp Alarm Vectors are: ", HI_TEMP, LO_TEMP, temp, 
            temp_alarm)
    
    humid_alarm = check_humidity(LO_HUMID, HI_HUMID, humidity, HUMID_ALARM_LED)
    print("High Humid, Low Humid, Humidity, & Humidity Alarm Vectors are: ", HI_HUMID, LO_HUMID, 
            humidity, humid_alarm)
    
    check_moisture(moisture, MOISTURE_ALARM_LED)
    print("Moisture is: ", moisture)

    smoke_alarm = check_gas(HI_DENSITY, density, BUZZER, SMOKE_ALARM_LED)
    print("High Density, Density, & Smoke Alarm Vectors are: ", HI_DENSITY, density, 
            smoke_alarm, SMOKE_ALARM_LED)
    