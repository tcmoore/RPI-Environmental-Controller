# send_values.py
# Todd Moore
# 3.9.19

# send values to various outputs, like file, RGB LCD, & STDIO

# ************  CODE IS WORKING!!   ************
 
# import grove_rgb_lcd
from grove_rgb_lcd import *
import time

def save_to_file(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on):

    # Values will be added as tab seperated delimited data with the following format:
    # datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
    # <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
    # hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

    # a new file is saved every hour
    fname = 'Values.txt'
    fmt ='%Y-%m-%d-%H'
    date_str = datetime.datetime.now().strftime(fmt)

    filename = date_str + "_" + fname
    # filename = "/home/pi/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"

    # concatenate data into 1 string argument
    values = data_time + "\t" + str(tempF) + "\t" + str(HI_TEMP) + "\t" + str(LO_TEMP) + \
            "\t" + str(humidity) + "\t" + humid_alarm + "\t" + str(moisture) + "\t" + moisture_alarm + \
            "\t" + str(density) + "\t" + str(HI_DENSITY) + "\t" + smoke_alarm + "\t" + fan_on + \
            "\t" + atomizer_on + "\n"

    print("Values being saved to file: ")
    print(values)

    # appends the values, then automatically closes the file for me
    with open(filename, "a") as myfile: 
        myfile.writelines(values)

# ----------------------------------------------------------------------------------------------------------
def print_to_stdio(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm,
                moisture, moisture_alarm, density, HI_DENSITY, smoke_alarm, fan_on, atomizer_on):

    # STDIO format is:
    #
    # Date/Time:    05/17/2019 05:27:00 
    #----------------------------------------------------------------------------------
    # temp alarm    NO      humid alarm NO      moisture alarm  PERFECT smoke_alarm NO
    # temp          70      humidity    70      moisture        500     density     800
    # hi temp       80      hi humid    80                              hi density  1000
    # low temp      65      low humid   60      
    #                           
    # fan on        NO      atomizer on NO  

    print("Date/Time    " + data_time)
    print("-----------------------------------------------------------------------------------------")
    print("temp alarm \t" + temp_alarm + "\t" + "humid alarm \t" + humid_alarm + "\t" + "moisture alarm \t" + moisture_alarm + "\t" + "smoke alarm \t" + smoke_alarm)
    print("temp \t" + "\t" + str(tempF) + " F\t" + "humidity \t" + str(humidity) + "%\t" + "moisture \t" + str(moisture) + "\t" + "density \t" + str(density))
    print("hi temp \t" + str(HI_TEMP) + " F\t" + "hi humid \t" + str(HI_HUMID) + "%\t\t\t\t" + "hi density \t" + str(HI_DENSITY))
    print("low temp \t" + str(LO_TEMP) + " F\t" + "low humid \t" + str(LO_HUMID)) + "%"
    print("")
    print("fan on \t\t" + fan_on + "\t" + "atomizer on \t" + atomizer_on)

def print_to_LCD(data_time, tempF, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm, density, smoke_alarm, 
               fan_on, atomizer_on):

#    ************  CODE IS NOT WORKING YET ************
 #   Display Environmental Data on LCD Screen
    #setRGB(0,128,64)
    setRGB(0,153,0)
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
