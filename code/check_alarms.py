# check_alarms.py
# Todd Moore
# 3.17.19
#!/usr/bin/env python
# coding=utf-8

# ******** WORKING AS OF 3.17.19 *****
# code that checks temp, humidity, soil moisture, & sets alarms if too high or too low.
# also checks Gas Density & sets smoke alarm if too high.

from grovepi import digitalWrite

def check_temp(LO_TEMP_ALARM, HI_TEMP_ALARM, temp, TEMP_ALARM_LED):
    # --------------------------------------------------------------------
    # check for temp alarm
    if HI_TEMP_ALARM > temp > LO_TEMP_ALARM:
        temp_alarm = "OFF"
        digitalWrite(TEMP_ALARM_LED, 0)     # turn off temp alarm led on RPI
        blynk_temp_led_color = "#FFF000"   # LED is RED on blynk app
    else:
        temp_alarm = "ON"
        digitalWrite(TEMP_ALARM_LED, 1)     # turn on temp alarm led on RPI
        blynk_temp_led_color = "#009900"   # LED is GREEN on blynk app
    # print("Temp Alarm is ", temp_alarm)
    # print("check_alarms.check_temp done")
    return temp_alarm, blynk_temp_led_color
    
def check_humidity(LO_HUMID_ALARM, HI_HUMID_ALARM, humidity, HUMID_ALARM_LED):
    # --------------------------------------------------------------------
    # check for humidity alarm
    if HI_HUMID_ALARM > humidity > LO_HUMID_ALARM:
        humid_alarm = "OFF"
        digitalWrite(HUMID_ALARM_LED, 0)     # turn off humidity alarm led        
        blynk_humid_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        humid_alarm = "ON"
        digitalWrite(HUMID_ALARM_LED, 1)     # turn on humidity alarm led     
        blynk_humid_led_color = "#FFF000"   # LED is RED on blynk app
    # print("Humid Alarm is ", humid_alarm)
    # print("check_alarms.check_humidity done")
    return humid_alarm, blynk_humid_led_color
        
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
        blynk_moist_led_color = "#CC6600"   # # LED is ORANGE on blynk app
    elif 424 >= moisture >= 18:
        moisture_alarm = 'DRY'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is dry & needs water!
        blynk_moist_led_color = "#CCCC00"   # # LED is YELLOW on blynk app
    elif 689 >= moisture >= 425:
        moisture_alarm = 'PERFECT'
        digitalWrite(MOISTURE_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!
        blynk_moist_led_color = "#009900"   # LED is GREEN on blynk app
    elif moisture >= 690:
        moisture_alarm = 'WATER'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is WET!!!
        blynk_moist_led_color = "#0000CC"   # LED is BLUE on blynk app
    else:
        moisture_alarm = 'BROKEN'
        digitalWrite(MOISTURE_ALARM_LED, 1)     # Turn on LED cause sensor is broken!!
        blynk_moist_led_color = "#FFF000"   # LED is RED on blynk app
    # print("Moisture Alarm is ",moisture_alarm)
    # print("check_alarms.check_moisture done")
    return moisture_alarm, blynk_moist_led_color
        
def check_gas(HI_DENSITY_ALARM, density, BUZZER, SMOKE_ALARM_LED):
    # check for smoke alarm
    if density < HI_DENSITY_ALARM:
        smoke_alarm = "OFF"
        digitalWrite(BUZZER, 0)     # Turn off buzzer       
        digitalWrite(SMOKE_ALARM_LED, 0)     # Turn off buzzer       
        blynk_smoke_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        smoke_alarm = "ON"
        digitalWrite(BUZZER, 1)     # Turn on buzzer
        digitalWrite(SMOKE_ALARM_LED, 0)     # Turn off buzzer       
        blynk_smoke_led_color = "#FFF000"   # LED is RED on blynk app
    # print("Smoke Alarm is ",smoke_alarm)
    # print("check_alarms.check_gas done")
    return smoke_alarm, blynk_smoke_led_color

# run main() function
if __name__ == "__main__":
    # -------- Test Vectors ------------
    # Hardware constants
    BUZZER = 2   
    HUMID_ALARM_LED = 3
    TEMP_ALARM_LED = 4
    SMOKE_ALARM_LED = 8
    MOISTURE_ALARM_LED = 9

    #Software constants
    HI_TEMP_ALARM = 80    # max allowable temp
    LO_TEMP_ALARM = 65    # min allowable temp
    HI_HUMID_ALARM = 85   # max allowable humidity percentage
    LO_HUMID_ALARM = 65   # min allowable humidity percentage
    HI_DENSITY_ALARM = 1000   # max allowable air density
    temp = 75
    humidity = 80
    moisture = 500
    density = 800
    temp_alarm = check_temp(LO_TEMP_ALARM, HI_TEMP_ALARM, temp, TEMP_ALARM_LED)
    print("High Temp, Low Temp, Temp, & Temp Alarm Vectors are: ", HI_TEMP_ALARM, LO_TEMP_ALARM, 
            temp, temp_alarm)
    
    humid_alarm = check_humidity(LO_HUMID_ALARM, HI_HUMID_ALARM, humidity, HUMID_ALARM_LED)
    print("High Humid, Low Humid, Humidity, & Humidity Alarm Vectors are: ", HI_HUMID_ALARM, 
            LO_HUMID_ALARM, humidity, humid_alarm)
    
    check_moisture(moisture, MOISTURE_ALARM_LED)
    print("Moisture is: ", moisture)

    smoke_alarm = check_gas(HI_DENSITY_ALARM, density, BUZZER, SMOKE_ALARM_LED)
    print("High Density, Density, & Smoke Alarm Vectors are: ", HI_DENSITY_ALARM, density, 
            smoke_alarm, SMOKE_ALARM_LED)
    