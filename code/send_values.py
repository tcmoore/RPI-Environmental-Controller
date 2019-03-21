# send_values.py
# Todd Moore
# 3.9.19
#!/usr/bin/env python
# coding=utf-8

# send values to various outputs, like file, RGB LCD, & STDIO

# ************  CODE IS WORKING!!   ************
 
from grove_rgb_lcd import *
import time
import datetime

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

    # a new file is saved every day
    fname = 'Values.txt'
    fmt ='%Y-%m-%d'
    date_str = datetime.datetime.now().strftime(fmt)

    filename = date_str + "_" + fname
    
    # concatenate data into 1 string argument
    values = data_time + "\t" + \
                str(tempF) + "\t" + \
                str(HI_TEMP_ALARM) + "\t" + \
                str(LO_TEMP_ALARM) + "\t" + \
                temp_alarm + "\t" + \
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
                str(hi_density_value) + "\t" + \
                str(lo_density_value) + "\t" + \
                smoke_alarm + "\t" + \
                fan_on + "\t" + \
                atomizer_on + "\n"

    print("Values being saved to file " + filename + ":" )
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
    # temp alarm    OFF     humid alarm OFF     moisture alarm  PERFECT smoke_alarm OFF
    # temp          70      humidity    70      moisture        500     density     800
    # hi temp       75      hi humid    75      hi moisture     500     hi density  900
    # lo temp       65      lo humid    62      lo moisture     400     lo density  875
    # hi alarm      80      hi alarm    80                              hi alarm    1000
    # low alarm     65      low alarm   60                              
     #                    
    # fan on        OFF      atomizer on OFF  

    print("Date/Time    " + data_time)
    print("-----------------------------------------------------------------------------------------")
    print("temp alarm \t" + temp_alarm + "\t" + "humid alarm \t" + humid_alarm + "\t" + "moisture alarm \t" + moisture_alarm + "\t" + "smoke alarm \t" + smoke_alarm)
    print("temp \t" + "\t" + str(tempF) + " F\t" + "humidity \t" + str(humidity) + "%\t" + "moisture \t" + str(moisture) + "\t" + "density \t" + str(density))
    print("hi alarm \t" + str(HI_TEMP_ALARM) + " F\t" + "hi alarm \t" + str(HI_HUMID_ALARM) + "%\t\t\t\t" + "hi alarm \t" + str(HI_DENSITY_ALARM))
    print("low alarm \t" + str(LO_TEMP_ALARM) + " F\t" + "low alarm \t" + str(LO_HUMID_ALARM)) + "%"
    print("hi temp \t" + str(hi_temp_value) + " F\t" + "hi humid \t" + str(hi_humid_value)) + "%\t" + "hi moisture \t" + str(hi_moisture_value) + "\thi density \t" + str(hi_density_value)
    print("lo temp \t" + str(lo_temp_value) + " F\t" + "lo humid \t" + str(lo_humid_value)) + "%\t"+ "lo moisture \t" + str(lo_moisture_value) + "\tlo density \t" + str(lo_density_value)
    print("")
    print("fan on \t\t" + fan_on + "\t" + "atomizer on \t" + atomizer_on + "\n")

def print_to_LCD(data_time, tempF, temp_alarm, hi_temp_value, lo_temp_value, humidity, 
                    humid_alarm, hi_humid_value, lo_humid_value, moisture, moisture_alarm, 
                    hi_moisture_value, lo_moisture_value, density, smoke_alarm, 
                    hi_density_value, lo_density_value, fan_on, atomizer_on):

#    ************  CODE IS NOT WORKING YET ************
 #   Display Environmental Data on LCD Screen
    setRGB(0,153,0) # display is green
    setText("Date/Time: \n" + str(data_time))
    time.sleep(2)

    if (temp_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Temp: " + str(tempF) + "F \nAlarm: " + temp_alarm)
    time.sleep(2)
    
    setRGB(0,153,0) # display is green
    setText("Hi Temp: " + str(hi_temp_value) + "F \nLo Temp: " + str(lo_temp_value) + "F")
    time.sleep(2)

    if (humid_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Humidity: " + str(humidity) + "% \nAlarm: " + humid_alarm)
    time.sleep(2)  

    setRGB(0,153,0) # display is green
    setText("Hi Humid: " + str(hi_humid_value) + "%\nLo Humid: " + str(lo_humid_value) + "%")
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
    setText("Moisture: " + str(moisture) + "\nAlarm: " + moisture_alarm)
    time.sleep(2)
    
    setRGB(0,153,0) # display is green
    setText("Hi Moist: " + str(hi_moisture_value) + "\nLo Moist: " + str(lo_moisture_value))
    time.sleep(2)

    if (smoke_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    
    setText("Density is " + str(density) + "%\nAlarm: " + smoke_alarm)
    time.sleep(2)

    setRGB(0,153,0) # display is green
    setText("Hi Dens: " + str(hi_density_value) + "%\nLo Dens: " + str(lo_density_value) + "%")
    time.sleep(2)

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
    temp_alarm = "ON"
    hi_temp_value = 80.0
    lo_temp_value = 50.0
    humidity = 75.0
    HI_HUMID_ALARM = 85.0   # max allowable humidity percentage
    LO_HUMID_ALARM = 65.0   # min allowable humidity percentage
    humid_alarm = "ON"
    hi_humid_value = 100.0
    lo_humid_value = 50.0
    moisture = 400
    moisture_alarm = "WATER"
    hi_moisture_value = 1000
    lo_moisture_value = 200
    density = 800
    HI_DENSITY_ALARM = 1000   # max allowable air density
    hi_density_value = 800
    lo_density_value = 300
    smoke_alarm = "ON"
    fan_on = "ON"
    atomizer_on = "ON"

    save_to_file(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on)

    print_to_stdio(data_time, tempF, HI_TEMP_ALARM, LO_TEMP_ALARM, temp_alarm, hi_temp_value,
                lo_temp_value, humidity, HI_HUMID_ALARM, LO_HUMID_ALARM, humid_alarm,  
                hi_humid_value, lo_humid_value, moisture, moisture_alarm, hi_moisture_value,
                lo_moisture_value, density, HI_DENSITY_ALARM, smoke_alarm, hi_density_value,
                lo_density_value, fan_on, atomizer_on)

    print_to_LCD(data_time, tempF, temp_alarm, hi_temp_value, lo_temp_value, humidity, 
                    humid_alarm, hi_humid_value, lo_humid_value, moisture, moisture_alarm, 
                    hi_moisture_value, lo_moisture_value, density, smoke_alarm, 
                    hi_density_value, lo_density_value, fan_on, atomizer_on)
