"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.
  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app
This example shows how to display custom data on the widget.
In your Blynk App project:
  Add a Value Display widget,
  bind it to Virtual Pin V2,
  set the read frequency to 1 second.
  Run the App (green triangle in the upper right corner).
It will automagically call v2_read_handler.
Calling virtual_write updates widget value.
"""
import datetime
import BlynkLib
# from BlynkTimer import BlynkTimer
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

# setup hi & low saved values
hi_temp_value = 0.0
lo_temp_value = 100.0
hi_humid_value = 0.0
lo_humid_value = 100.0
hi_moisture_value = 0.0
lo_moisture_value = 1000.0
hi_density_value = 0.0
lo_density_value = 1000.0

BLYNK_AUTH = '9f4faa38d423494fb9c711144e5fea1f'

# Setup Hardware
setup_rpi.hardware(BUZZER, GAS_SENSOR, MOISTURE_SENSOR, TEMP_SENSOR, ATOMIZER, LIGHT, FAN, 
                    TEMP_ALARM_LED, HUMID_ALARM_LED, MOISTURE_ALARM_LED, ATOMIZER_ON_LED)

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
# timer = BlynkTimer()
    
# Register virtual pin handler
# @blynk.VIRTUAL_READ(0)  # time value

# temp
# @blynk.VIRTUAL_READ(1)  # temp value
# @blynk.VIRTUAL_READ(2)  # hi temp value
# @blynk.VIRTUAL_READ(3)  # low temp value
# @blynk.VIRTUAL_READ(4)  # hi temp alarm value
# @blynk.VIRTUAL_READ(5)  # low temp alarm value
# @blynk.VIRTUAL_READ(6)  # temp alarm led
# humidity
# @blynk.VIRTUAL_READ(7)  # humidity value
# @blynk.VIRTUAL_READ(8)  # hi humidity value
# @blynk.VIRTUAL_READ(9)  # low humidity value
# @blynk.VIRTUAL_READ(10)  # hi humid alarm value
# @blynk.VIRTUAL_READ(11) # lo humid alarm value
# @blynk.VIRTUAL_READ(12) # humid alarm LED

# moisture
# @blynk.VIRTUAL_READ(13)  # moisture value
# @blynk.VIRTUAL_READ(14)  # hi moisture value
# @blynk.VIRTUAL_READ(15)  # lo moisture value
# @blynk.VIRTUAL_READ(16)  # moisture alarm value
# @blynk.VIRTUAL_READ(17)  # moisture alarrm LED

# density
# @blynk.VIRTUAL_READ(18)  # density value
# @blynk.VIRTUAL_READ(19)  # hi density value
# @blynk.VIRTUAL_READ(20)  # lo density value
# @blynk.VIRTUAL_READ(21)  # hi density alarm value
# @blynk.VIRTUAL_READ(22)  # density alarm LED
 
# equipment control
# @blynk.VIRTUAL_READ(23)  # fan on LED
# @blynk.VIRTUAL_READ(24) # atomizer on LED
# @blynk.VIRTUAL_READ(25) # light on LED

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
hi_temp_value1, lo_temp_value1 = hi_lo_values.hi_lo_temp(tempF, hi_temp_value, lo_temp_value)
hi_humid_value1, lo_humid_value1 = hi_lo_values.hi_lo_humid(humidity, hi_humid_value, lo_humid_value)
hi_moisture_value1, lo_moisture_value1 = hi_lo_values.hi_lo_moisture(moisture, hi_moisture_value, 
                                                                        lo_moisture_value)
hi_density_value1, lo_density_value1 = hi_lo_values.hi_lo_density(density, hi_density_value, 
                                                                    lo_density_value)
# ____________________________________________________________________________________

# check for alarms
temp_alarm, blynk_temp_led_color = check_alarms.check_temp(LO_TEMP_ALARM, HI_TEMP_ALARM, tempF, 
                                                                TEMP_ALARM_LED)
humid_alarm, blynk_humid_led_color = check_alarms.check_humidity(LO_HUMID_ALARM, HI_HUMID_ALARM, humidity, 
                                                                    HUMID_ALARM_LED)
moisture_alarm, blynk_moist_led_color = check_alarms.check_moisture(moisture, MOISTURE_ALARM_LED)
smoke_alarm, blynk_smoke_led_color = check_alarms.check_gas(HI_DENSITY_ALARM, density, BUZZER, 
                                                                SMOKE_ALARM_LED)
# ____________________________________________________________________________________
# turn on/off equipment           
# Turn Fan on if temperature is too high or humidity is too high
fan_on, blynk_fan_led_color = control.fan(tempF, humidity, FAN_HI_TEMP, FAN_LO_TEMP, FAN_HI_HUMID, 
                                            FAN_LO_HUMID, FAN)
        
# turn on water atomizer if humidity is too low
atomizer_on, blynk_atomizer_led_color = control.atomizer(humidity, ATOMIZER, ATOMIZER_LO_HUMIDITY, 
                                                            ATOMIZER_ON_LED)
        
# turn on/off lights based on a certain time
light_on, blynk_light_led_color = control.light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)
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

# map virtual pins to data values
# date/time value
blynk.virtual_write(0, data_time) 
#temp values
blynk.virtual_write(1, str(tempF))
# blynk.virtual_write(2, str(hi_temp_value))
# blynk.virtual_write(3, str(lo_temp_value))
# blynk.virtual_write(4, str(HI_TEMP_ALARM))
# blynk.virtual_write(5, str(LO_TEMP_ALARM))
blynk.set_property(6, "color", blynk_temp_led_color)
blynk.virtual_write(6, "255")
# #humidity values
# blynk.virtual_write(7, str(humidity))
# blynk.virtual_write(8, str(hi_humid_value))
# blynk.virtual_write(9, str(lo_humid_value))
# blynk.virtual_write(10, str(HI_HUMID_ALARM))
# blynk.virtual_write(11, str(LO_HUMID_ALARM))
blynk.set_property(12, "color", blynk_humid_led_color)
blynk.virtual_write(12, "255")
 # # moisture values
# blynk.virtual_write(13, moisture) 
# blynk.virtual_write(14, str(hi_moisture_value))
# blynk.virtual_write(15, str(lo_moisture_value))
# blynk.virtual_write(16, str(moisture_alarm))
blynk.set_property(17, "color", blynk_moist_led_color)
blynk.virtual_write(17, "255")
# density values
# blynk.virtual_write(18, str(density))
# blynk.virtual_write(19, str(hi_density_value))
# blynk.virtual_write(20, str(lo_density_value))
# blynk.virtual_write(21, str(HI_DENSITY_ALARM))
blynk.set_property(22, "color", blynk_smoke_led_color)
blynk.virtual_write(22, "255")
# equipment control signals
# blynk.set_property(23, "color", blynk_fan_led_color)
# blynk.virtual_write(23, "255")
# blynk.set_property(24, "color", blynk_atomizer_led_color)
# blynk.virtual_write(24, "255")
# blynk.set_property(25, "color", blynk_light_led_color)
# blynk.virtual_write(25, "255")
    
# Add Timers
# timer.set_interval(0.1, read_handler)

# while True:
# #    read_handler() 
#     blynk.run()
#     timer.run()
