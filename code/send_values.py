# send_values.py
# Todd Moore
# 3.9.19
#!/usr/bin/env python
# coding=utf-8

# send values to various outputs, like file, RGB LCD, & STDIO

# ************  CODE IS WORKING!!   ************
 
from grove_rgb_lcd import *
import time

def save_to_file(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on):

    # Values will be added as tab seperated delimited data with the following format:
    # datetime  temp    hi temp alarm   low temp alarm  temp_alarm  hi temp value   low temp value
    # humidity  hi humidity alarm   low humidity alarm  humidity alarm  hi humidity value
    # lo humidity value moisture  hi moisture alarm   low moisture alarm  moisture alarm  
    # hi moisture value lo moisture value   density   hi density alarm    hi density value    
    # lo density value  smoke alarm   fan on  ataomizer on

    # a new file is saved every hour
    fname = 'Values.txt'
    fmt ='%Y-%m-%d-%H'
    date_str = datetime.datetime.now().strftime(fmt)

    filename = date_str + "_" + fname
    
    # concatenate data into 1 string argument
    values = data_time + "\t" + \
                str(tempF) + "\t" + \
                str(HI_TEMP_ALARM) + "\t" + \
                str(LO_TEMP_ALARM) + "\t" + \
                (temp_alarm) + "\t" + \
                str(hi_temp_value) + "\t" + \
                str(lo_temp_value) + "\t" + \
                str(humidity) + "\t" + \
                str(HI_HUMID_ALARM) + "\t" + \
                str(LO_HUMID_ALARM) + "\t" + \
                humid_alarm + "\t" + \
                str(hi_humid_value) + "\t" + \
                str(lo_humid_value) + "\t" + \
                str(moisture) + "\t" + \
                moisture_alarm + "\t" + \
                str(hi_moisture_value) + "\t" + \
                str(lo_moisture_value) + "\t" + \
                str(density) + "\t" + \
                str(HI_DENSITY_ALARM) + "\t" + \
                smoke_alarm + "\t" + \
                fan_on + "\t" + \
                atomizer_on + "\n"

    print("Values being saved to file: ")
    print(values)

    # appends the values, then automatically closes the file for me
    with open(filename, "a") as myfile: 
        myfile.writelines(values)

# ----------------------------------------------------------------------------------------------------------
def print_to_stdio(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on):

    # STDIO format is:
    #
    # Date/Time:    05/17/2019 05:27:00 
    #----------------------------------------------------------------------------------
    # temp alarm    NO      humid alarm NO      moisture alarm  PERFECT smoke_alarm NO
    # temp          70      humidity    70      moisture        500     density     800
    # hi alarm      80      hi alarm    80      hi moisture     500     hi alarm    1000
    # low alarm     65      low alarm   60      lo moisture     400     hi density  900
    # hi temp       75      hi humid    75                              lo density  875
    # lo temp       65      lo humid    62
    #                    
    # fan on        NO      atomizer on NO  

    print("Date/Time    " + data_time)
    print("-----------------------------------------------------------------------------------------")
    print("temp alarm \t" + temp_alarm + "\t" + "humid alarm \t" + humid_alarm + "\t" + "moisture alarm \t" + moisture_alarm + "\t" + "smoke alarm \t" + smoke_alarm)
    print("temp \t" + "\t" + str(tempF) + " F\t" + "humidity \t" + str(humidity) + "%\t" + "moisture \t" + str(moisture) + "\t" + "density \t" + str(density))
    print("hi temp \t" + str(HI_TEMP_ALARM) + " F\t" + "hi humid \t" + str(HI_HUMID_ALARM) + "%\t\t\t\t" + "hi density \t" + str(HI_DENSITY_ALARM))
    print("low temp \t" + str(LO_TEMP_ALARM) + " F\t" + "low humid \t" + str(LO_HUMID_ALARM)) + "%"
    print("")
    print("fan on \t\t" + fan_on + "\t" + "atomizer on \t" + atomizer_on)

def print_to_LCD(data_time, tempF, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm, density, smoke_alarm, 
               fan_on, atomizer_on):

#    ************  CODE IS NOT WORKING YET ************
 #   Display Environmental Data on LCD Screen
    setRGB(0,153,0) # display is green
    setText("Date/Time: \n" + str(data_time))
    time.sleep(2)

    if (temp_alarm == "YES"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Temp:" + str(tempF) + " F \nAlarm:" + temp_alarm)
    time.sleep(2)
    
    if (humidity_alarm == "YES"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Humidity:" + str(humidity) + "% \nAlarm:" + humidity_alarm)
    time.sleep(2)       
    
    if (moisture_alarm == "AIR"):
        setRGB(204,102,0) # display is orange
    elif (moisture_alarm == "DRY"):
        setRGB(204,204,0) # display is yellow
    elif (moisture_alarm == "PERFECT"):
        setRGB(0,153,0) # display is green
    elif (moisture_alarm == "WATER"):
        setRGB(0,0,204) # display is dark blue
    else:
        setRGB(255,0,0) # alarm - display is red
    setText("Moisture: " + str(moisture) + " \nAlarm:" + moisture_alarm)
    time.sleep(2)
    
    if (smoke_alarm == "YES"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Density is " + str(density) + "% \nAlarm:" + smoke_alarm)
    time.sleep(2)

    setRGB(0,153,0) # display back to green
    setText("Fan is " + fan_on)
    time.sleep(2)

    setText("Atomizer is " + atomizer_on)
    
# run main() function
if __name__ == "__main__":
    import datetime
    # -------- Test Vectors ------------
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Data Date/Time is ", data_time)

    tempF = 75.0
    HI_TEMP_ALARM = 80.0    # max allowable temp
    LO_TEMP_ALARM = 65.0    # min allowable temp
    temp_alarm = "YES"
    humidity = 75.0
    HI_HUMID_ALARM = 85.0   # max allowable humidity percentage
    LO_HUMID_ALARM = 65.0   # min allowable humidity percentage
    humid_alarm = "YES"
    moisture = 400
    moisture_alarm = "WATER"
    density = 800
    HI_DENSITY_ALARM = 1000   # max allowable air density
    smoke_alarm = "YES"
    fan_on = "YES"
    atomizer_on = "YES"
    save_to_file(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY_ALARM, smoke_alarm, fan_on, atomizer_on)

    print_to_stdio(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY_ALARM, smoke_alarm, fan_on, atomizer_on)

    print_to_LCD(data_time, tempF, temp_alarm, humidity, humid_alarm, moisture, moisture_alarm, density, smoke_alarm,
                fan_on, atomizer_on)
