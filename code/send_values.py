# send_values.py
# Todd Moore
# 3.9.19

# send values to various outputs, like file, RGB LCD, & STDIO
 
import grove_rgb_lcd

def save_to_file(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on):

	# ************	CODE IS WORKING!!	************

	# Values will be added as tab seperated delimited data with the following format:
	# datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
	# <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
	# hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

	filename = "/home/pi/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"

	# concatenate data into 1 string argument
	values = data_time + "\t" + str(tempF) + "\t" + str(HI_TEMP) + "\t" + str(LO_TEMP) + "\t" + humid_alarm + "\t"\
		+ str(moisture) + "\t" + str(HI_MOISTURE) + "\t", str(LO_MOISTURE) + "\t" + moisture_alarm + "\t" + str(density) + "\t"\
		+ str(HI_DENSITY) + "\t" + smoke_alarm + "\t" + fan_on + "\t" + atomizer_on + "\n"

	print("Values being saved to file: ")
	print(values)

	# appends the values, then automatically closes the file for me
	with open(filename, "a") as myfile: 
		myfile.writelines(values)

# -----------------------------------------------------------------------------------------------------------------
def print_to_stdio(data_time, tempF, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on):

	# ************	CODE IS WORKING!!	************

	# STDIO format is:
	#
	# Date/Time: 	05/17/2019 05:27:00	
	#--------------------------------------------------------------
	# temp alarm	NO		humid alarm	NO		moisture alarm	HUMID	smoke_alarm	NO
	# temp			70		humidity	70		moisture		500		density		800
	# hi temp		80		hi humid	80								hi density	1000
	# low temp		65		low humid	60		
	#							
	# fan on		NO		
	# atomizer on	NO			

	print("\n")
	print("Date/Time	" + data_time)
	print("-------------------------------------------------------------------------------------------------------")
	print("temp alarm \t" + temp_alarm + "humid alarm \t" + humid_alarm + "\t" = "moisture alarm \t" + moisture_alarm + "\t" + "smoke alarm \t" + smoke_alarm)
	print("temp \t") + "\t" + "\t" + str(temp) + "\t" + "humidity \t" + "\t" + str(humidity) + "\t" + "moisture \t" + str(moisture) + "\t" + "density \t" + str(density))
	print("hi temp \t" + str(HI_TEMP) + "\t" + "hi humid \t" + str(HI_HUMID) + "\t" + "hi moisture \t" + str(HI_MOISTURE))
	print("low temp \t" + str(LO_TEMP) + "\t" + "low humid \t" + str(LO_HUMID) + "\t" + "low moisture \t" + str(LO_MOISTURE))
	
	
	 str(tempF) + "\t" + "humidity \t" + str(humidity) + "\t" + "moisture \t" + str(moisture))
	print("temp \t" +"\t" + str(tempF) + "\t" + "humidity \t" + str(humidity) + "\t" + "moisture \t" + str(moisture))
	print("\n")
	print("density \t" + str(density) + "\t" + "fan on \t" + fan_on + "\t" + "smoke alarm \t" + smoke_alarm)
	print("hi density \t" + str(HI_DENSITY) + "\t" + "atomizer on \t" + atomizer_on)

def print_to_LCD(data_time, temp, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm, density, smoke_alarm, 
				fan_on, atomizer_on):

	# ************	CODE IS NOT WORKING YET	************
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

# run main() function
if __name__ == "__main__":
	print("Executing as main program")
	print("Value of __name__ is: ", __name__)
	import datetime
	# -------- Test Vectors ------------
	data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	print("Data Date/Time is ", data_time)

	temp = 75
	HI_TEMP = 80	# max allowable temp
	LO_TEMP = 65	# min allowable temp
	temp_alarm = "YES"
	humidity = 75
	HI_HUMID = 85	# max allowable humidity percentage
	LO_HUMID = 65	# min allowable humidity percentage
	humid_alarm = "YES"
	moisture = 400
	HI_MOISTURE = 700	# max allowable soil moisture level
	LO_MOISTURE = 300	# min allowable soil moisture level
	moisture_alarm = "YES"
	density = 800
	HI_DENSITY = 1000	# max allowable air density
	smoke_alarm = "YES"
	fan_on = "YES"
	atomizer_on = "YES"
	save_to_file(data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on)
	print_to_stdio(data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humid_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on)
	# print_to_LCD(data_time, temp, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm, density, smoke_alarm, 
	# 			fan_on, atomizer_on)
