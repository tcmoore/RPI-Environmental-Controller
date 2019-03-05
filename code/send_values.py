# send values to various outputs, like file, RGB LCD, & STDIO

# Todd Moore
# 3.4.19

import grove_rgb_lcd

def save_to_file(data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on)
	# ************	CODE IS WORKING IN SENSOR_TESTING FOLDER!!	************

	# Values will be added as tab seperated delimited data with the following format:
	# datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
	# <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
	# hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

	filename = "/home/pi/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"

	# concatenate data into 1 string argument
	values = data_time + "\t" + str(temp) + "\t" + str(HI_TEMP) + "\t" + str(LO_TEMP) + "\t" + humid_alarm + "\t"\
		+ str(moisture) + "\t" + str(HI_MOISTURE) + "\t", str(LO_MOISTURE) + "\t" + moisture_alarm + "\t" + str(density) + "\t"\
		+ str(HI_DENSITY) + "\t" + smoke_alarm + "\t" + fan_on + "\t" + atomizer_on + "\n"

	print(values)

	# appends the values, then automatically closes the file for me
	with open(filename, "a") as myfile: 
    	myfile.writelines(values)

# -----------------------------------------------------------------------------------------------------------------
def print_to_stdio(format_now, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humidity_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on)

	# ************	CODE IS WORKING IN SENSOR_TESTING FOLDER!!	************

	# STDIO format is:
	#
	# Date/Time: 	05/17/2019 05:27:00	
	#--------------------------------------------------------------
	# temp			70		humidity	70		moisture		500
	# hi temp		80		hi humid	80		hi moisture		700
	# low temp		65		low humid	60		low moisture	300
	# temp alarm	NO		humid alarm	NO		moisture alarm	NO
	#							
	# density		800		fan on		NO		smoke_alarm		NO
	# hight density	1000	atomizer on	NO			

	print("\n")
	print("Date/Time	" + data_time)
	print("-------------------------------------------------------------------------------------------------------")
	print("temp \t" +"\t" + str(temp) + "\t" + "humidity \t" + str(humidity) + "\t" + "moisture \t" + str(moisture))
	print("hi temp \t" + str(HI_TEMP) + "\t" + "hi humid \t" + str(HI_HUMID) + "\t" + "hi moisture \t" + str(HI_MOISTURE))
	print("low temp \t" + str(LO_TEMP) + "\t" + "low humid \t" + str(LO_HUMID) + "\t" + "low moisture \t" + str(LO_MOISTURE))
	print("\n")
	print("density \t" + str(density) + "\t" + "fan on \t" + fan_on + "\t" + "smoke alarm \t" + smoke_alarm)
	print("hi density \t" + str(HI_DENSITY) + "\t" + "atomizer on \t" + atomizer_on)

def print_to_LCD(data_time, temp, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm, density, smoke_alarm, 
				fan_on, atomizer_on)

	# --------------------------------------------------------------------
	# Display Environmental Data on LCD Screen
	setRGB(0,128,64)
    	time.sleep(1)
	setText("Date/Time: ", data_time)
    	time.sleep(1)
	setText("Temp:",str(temp)," F - Alarm:",temp_alarm)
    	time.sleep(1)
	setText("Humidity:",str(humidity),"% - Alarm:",humidity_alarm,"Atomizer is ",atomizer_on) 
    	time.sleep(1)		
	setText("Moisture: ", str(moisture)," - Alarm:",moisture_alarm)
    	time.sleep(1)
	setText("Density is ",str(density), "% - Alarm:", smoke_alarm)
    	time.sleep(1)
	setText("Fan is ",fan_on)
    	time.sleep(1)
	setText("Atomizer is ", atomizer_on)
	time.sleep(5)	