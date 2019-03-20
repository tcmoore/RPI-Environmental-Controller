# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 3.16.19

# code that measures temp, humidity, & soil moisture (for 2 plants), sets alarms, saves alarm data, 
# increases humidity in growbox,& displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions

#   Port #  Pins on Port #  Type                Sensor Pin  Sensor/Module
#   ------------------------------------------------------------------------
#   SERIAL  D0 & D1         DIGITAL & SERIAL                n/a
#   D2      D2 & D3         DIGITAL             D2          Grove Buzzer
#   D3      D3 & D4         DIGITAL             D3          Humid Alarm LED
#                                               D4          Temp Alarm LED
#   D4      D4 & D5         DIGITAL             n/a
#   D5      D5 & D6         DIGITAL             D5          Water Atomizer LED
#   D6      D6 & D7         DIGITAL             D6          Grove - Temperature&Humidity Sensor Pro
#   D7      D7 & D8         DIGITAL             D7          Grove - Water Atomization
#   D8      D8 & D9         DIGITAL             D8          Smoke Alarm LED
#                                               D9          Moisture Alarm LED
#                   
#   A0      A0 & A1         ANALOG              A0          Grove - Moisture Sensor
#   A1      A1 & A2         ANALOG              A1          Grove MQ2 Air Sensor
#   A2      A2 & A3         ANALOG              D16         Grove - 2-Channel SPDT Switch 1,
#                                                               LED Lights
#                                               D17         Grove - 2-Channel SPDT Switch 2,
#                                                               Exhaust Fan
#
#   I2C-1   I2C                                             Free
#   I2C-2   I2C                                             Free
#   I2C-3   I2C                                             Grove - LCD RGB Backlight
#   RPRISER                 RPI SERIAL          

#!/usr/bin/env python
# coding=utf-8

import datetime
import time
import setup_rpi
import get
import hi_lo_values
import check_alarms
import control
import send_values

# --------------Setup Constants ---------------------
# GrovePi+ Hat Digital Pin Constants
BUZZER = 2          
HUMID_ALARM_LED = 3
TEMP_ALARM_LED = 4
ATOMIZER_ON_LED = 5
TEMP_SENSOR = 6
ATOMIZER = 7
SMOKE_ALARM_LED = 8
MOISTURE_ALARM_LED = 9
LIGHT = 16  # uses A2 as digital channels 16 & 17
FAN = 17    # uses A2 as digital channels 16 & 17

# GrovePi+ Hat Analog Pin Constants
MOISTURE_SENSOR = 0
GAS_SENSOR = 1  

# temp_humidity_sensor_type
# This represents the cover color of the sensor. I have the white type.
#BLUE = 0    # The Blue colored sensor.
WHITE = 1   # The White colored sensor.

#Software constants
HI_TEMP_ALARM = 80.0    # max allowable temp
LO_TEMP_ALARM = 40.0    # min allowable temp
HI_HUMID_ALARM = 85.0   # max allowable humidity percentage
LO_HUMID_ALARM = 25.0   # min allowable humidity percentage
HI_DENSITY_ALARM = 1000 # max allowable density number
FAN_HI_TEMP = 80.0    # max allowable temp
FAN_LO_TEMP = 65.0    # min allowable temp
FAN_HI_HUMID = 85.0   # max allowable humidity percentage
FAN_LO_HUMID = 65.0   # min allowable humidity percentage
ATOMIZER_LO_HUMIDITY = 65   # humidity level water atomizer turns on
LIGHT_START = '5:00'    # turn on light @ 5AM
LIGHT_STOP = '17:00'    # turn off light @ 5PM

# Setup Hardware
setup_rpi.hardware(BUZZER, GAS_SENSOR, MOISTURE_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, 
                    TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED, ATOMIZER_ON_LED)

# setup hi & low saved values
hi_temp_value = 0.0
lo_temp_value = 100.0
hi_humid_value = 0.0
lo_humid_value = 100.0
hi_moisture_value = 0.0
lo_moisture_value = 1000.0
hi_density_value = 0.0
lo_density_value = 1000.0

while True:
    # Get current date & times
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print("Data Date/Time is ", data_time)
    minutes = datetime.datetime.now().strftime("%M")
    # print("Minutes is ", minutes)
    light_time = datetime.datetime.now().strftime("%H:%M")  # Only need hours:minutes
    # print("Light Date/Time is ", light_time)
# ____________________________________________________________________________________
    # Get sesor data...
    # Get Temperature in F & Humidity
    tempF, humidity = get.temp(TEMP_SENSOR, WHITE)
                
    # Get Soil Moisture & check if there is an alarm
    #   Here are suggested sensor values:
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water
    
    #   Sensor values observer: 
    #       Values  Condition
    #       --------------------------
    #       0-17    sensor in open air
    #       18-424  sensor in dry soil
    #       425-689 sensor in humid soil
    #       690+    sensor in water
    moisture = get.moisture(MOISTURE_SENSOR)
                    
    # Get Air Quality Value from MQ2 sensor
    density = round(get.air(GAS_SENSOR), 2)
# ____________________________________________________________________________________
    # save the hi & low values 
    hi_temp_value, lo_temp_value = hi_lo_values.hi_lo_temp(tempF, hi_temp_value, lo_temp_value)
    hi_humid_value, lo_humid_value = hi_lo_values.hi_lo_humid(humidity, hi_humid_value, lo_humid_value)
    hi_moisture_value, lo_moisture_value = hi_lo_values.hi_lo_moisture(moisture, hi_moisture_value, lo_moisture_value)
    hi_density_value, lo_density_value = hi_lo_values.hi_lo_density(density, hi_density_value, lo_density_value)
# ____________________________________________________________________________________
    # check for alarms
    temp_alarm = check_alarms.check_temp(LO_TEMP_ALARM, HI_TEMP_ALARM, tempF, TEMP_ALARM_LED)
    humid_alarm = check_alarms.check_humidity(LO_HUMID_ALARM, HI_HUMID_ALARM, humidity, 
                                                HUMID_ALARM_LED)
    moisture_alarm = check_alarms.check_moisture(moisture, MOISTURE_ALARM_LED)
    smoke_alarm = check_alarms.check_gas(HI_DENSITY_ALARM, density, BUZZER, SMOKE_ALARM_LED)
# ____________________________________________________________________________________
    # turn on/off equipment           
    # Turn Fan on if temperature is too high or humidity is too high
    fan_on = control.fan(tempF, humidity, FAN_HI_TEMP, FAN_LO_TEMP, FAN_HI_HUMID, FAN_LO_HUMID, 
                            FAN)
            
    # turn on water atomizer if humidity is too low
    atomizer_on = control.atomizer(humidity, ATOMIZER, ATOMIZER_LO_HUMIDITY, ATOMIZER_ON_LED)
            
    # turn on/off lights based on a certain time
    light_on = control.light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)
# ____________________________________________________________________________________
    # save & send values
    # Append values to a file every 15 min. a new file is created every day.
    if (minutes == "00" or minutes == "15" or minutes == "30" or minutes == "45"):
        send_values.save_to_file(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on)
    
    # append file to a file if there is an error.
    if (temp_alarm == "ON" or humid_alarm == "ON" or moisture_alarm == "AIR" or moisture_alarm == "DRY" 
            or moisture_alarm == "WATER" or smoke_alarm == "ON"):
        send_values.save_to_file(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on)

    # Print values to std out console
    send_values.print_to_stdio(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on)

    # Display Environmental Data on LCD Screen
    send_values.print_to_LCD(data_time, tempF, temp_alarm, hi_temp_value, lo_temp_value, humidity, 
                    humid_alarm, hi_humid_value, lo_humid_value, moisture, moisture_alarm, 
                    hi_moisture_value, lo_moisture_value, density, smoke_alarm, 
                    hi_density_value, lo_density_value, fan_on, atomizer_on)
            
    # wait for 30 seconds before taking another set of data (19 seconds for lcd output &
    # 2 seconds below = the 15 seconds)
    time.sleep(9)
