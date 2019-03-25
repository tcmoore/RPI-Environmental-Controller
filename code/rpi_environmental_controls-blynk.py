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
import BlynkLib
import setup_rpi
import get
import hi_lo_values
import check_alarms
import control
import send_values
import config

########
# Setup Hardware
########
setup_rpi.hardware()

########
# Welcome Screen on LCD
########
send_values.version_to_lcd()

########
# Initialize Blynk
########
blynk = BlynkLib.Blynk(config.BLYNK_AUTH)

########
# register virtual pins for the blynk app
########
# use the new command, '@blynk.ON()', instead of '@blynk.VIRTUAL_READ()'
@blynk.ON(0)
@blynk.ON(1)
@blynk.ON(2)
@blynk.ON(7)
@blynk.ON(16)

def v0_read_handler():
    # Get current date & times
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print("Data Date/Time is ", data_time)
    minutes = datetime.datetime.now().strftime("%M")
    # print("Minutes is ", minutes)
    light_time = datetime.datetime.now().strftime("%H:%M")  # Only need hours:minutes
    # print("Light Date/Time is ", light_time)
    #__________________________________________________________________________________

    # Get sesor data...
    # Get Temperature in F & Humidity
    get.temp()

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
    get.moisture()

    # Get Air Quality Value from MQ2 sensor
    get.air()
#    config.density = round(get.air(config.GAS_SENSOR), 2)
    #__________________________________________________________________________________

    # save the hi & low values 
    hi_lo_values.hi_lo_temp()
    hi_lo_values.hi_lo_humid()
    hi_lo_values.hi_lo_moisture()
    hi_lo_values.hi_lo_density()
    #__________________________________________________________________________________

    # check for alarms
    check_alarms.check_temp()
    check_alarms.check_humidity()
    check_alarms.check_moisture()
    check_alarms.check_gas()
    #__________________________________________________________________________________

    # turn on/off equipment           
    # Turn Fan on if temperature is too high or humidity is too high
    control.fan()
                                            
    # turn on water atomizer if humidity is too low
    control.atomizer()

    # turn on/off lights based on a certain time
    control.light(light_time)
    #__________________________________________________________________________________

    # save & send values
    # append values to a file every 15 min. a new file is created every day.
    if (minutes == "00" or minutes == "15" or minutes == "30" or minutes == "45"):
        send_values.save_to_file(data_time)

    # append values to a file if there is an error.
    if (config.temp_alarm == "ON" or config.humid_alarm == "ON" or config.moisture_alarm == "AIR" or
             config.moisture_alarm == "DRY" or config.moisture_alarm == "WATER" or 
             config.smoke_alarm == "ON"):
        send_values.save_to_file(data_time)
                                
    # print values to std out console
    send_values.print_to_stdio(data_time)

    # output values to the RGB LCD
    
    send_values.print_to_LCD(data_time)
    #__________________________________________________________________________________

    # map virtual pins to data values
    # date/time value
    blynk.set_property(0, "label", "DATE TIME")
    blynk.virtual_write(0, data_time)
    
    #temp values
    blynk.set_property(1, "label", "CURRENT TEMP")
    blynk.set_property(1, "color", config.blynk_temp_led_color)
    blynk.virtual_write(1, str(config.tempF))

    blynk.set_property(2, "label", "HI TEMP TODAY")
    blynk.set_property(2, "color", "#FFD700")   # display is gold for higher temp
    blynk.virtual_write(2, str(config.hi_temp_value))
    # blynk.virtual_write(3, str(lo_temp_value))
    # blynk.virtual_write(4, str(HI_TEMP_ALARM))
    # blynk.virtual_write(5, str(LO_TEMP_ALARM))
 
    # #humidity values
    blynk.set_property(7, "label", "CURRENT HUMIDITY")
    blynk.set_property(7, "color", config.blynk_humid_led_color)
    blynk.virtual_write(7, str(config.humidity))
    # blynk.virtual_write(8, str(hi_humid_value))
    # blynk.virtual_write(9, str(lo_humid_value))
    # blynk.virtual_write(10, str(HI_HUMID_ALARM))
    # blynk.virtual_write(11, str(LO_HUMID_ALARM))

    # # moisture values
    # blynk.virtual_write(13, str(moisture))
    # blynk.virtual_write(14, str(hi_moisture_value))
    # blynk.virtual_write(15, str(lo_moisture_value))
    # blynk.set_property(16, "label", config.moisture_alarm)
    # blynk.set_property(16, "color", config.blynk_moist_led_color)
    # blynk.virtual_write(16, config.moisture)

    # # density values
    # blynk.virtual_write(17, str(density))
    # blynk.virtual_write(18, str(hi_density_value))
    # blynk.virtual_write(19, str(lo_density_value))
    # blynk.virtual_write(20, str(HI_DENSITY_ALARM))
    # blynk.virtual_write(21, str(smoke_alarm))

    # # equipment control signals
    # blynk.virtual_write(22, str(fan_on))
    # blynk.virtual_write(23, str(atomizer_on))
    # blynk.virtual_write(24, str(light_on))
    # blynk.virtual_write(25, smoke_led)

    # Add Timers
    # timer.set_interval(1, v0_read_handler)
 
while True:
    v0_read_handler()
    blynk.run()
#    time.sleep(3)
#     timer.run()
