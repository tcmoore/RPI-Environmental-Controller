# hi_low_avg_values.py
# Todd Moore
# 3.9.19

# save high, low, & average values of temp, humidity, moisture, & density to variables

# ************  CODE IS WORKING!!   ************
 
# import grove_rgb_lcd
from grove_rgb_lcd import *
import time

def all_values(tempF, humidity, moisture, density):
    # hi temperature value
    if tempF > hi_temp_value:
        hi_temp_value = tempF
    else:
        hi_temp_value = hi_temp_value
    
 # low temperature value
    if tempF < lo_temp_value:
        lo_temp_value = tempF
    else:
        lo_temp_value = lo_temp_value
    
# hi humidity value
    if humidity > hi_humid_value:
        hi_humid_value = humidity
    else:
        hi_humid_value = hi_humid_value
    
 # low humidity value
    if humidity < lo_humid_value:
        lo_humid_value = tempF
    else:
        lo_humid_value = lo_humid_value
    
# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    import datetime
    # -------- Test Vectors ------------
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Data Date/Time is ", data_time)

    tempF = 75.0
    HI_TEMP = 80.0    # max allowable temp
    LO_TEMP = 65.0    # min allowable temp
    temp_alarm = "YES"
    humidity = 75.0
    HI_HUMID = 85.0   # max allowable humidity percentage
    LO_HUMID = 65.0   # min allowable humidity percentage
    humid_alarm = "YES"
    moisture = 400
    moisture_alarm = "WATER"
    density = 800
    HI_DENSITY = 1000   # max allowable air density
    smoke_alarm = "YES"
    fan_on = "YES"
    atomizer_on = "YES"
    save_to_file(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on)

    print_to_stdio(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on)

    print_to_LCD(data_time, tempF, temp_alarm, humidity, humid_alarm, moisture, moisture_alarm, density, smoke_alarm,
                fan_on, atomizer_on)
