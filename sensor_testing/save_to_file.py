

main()
	# Values will be added as tab seperated delimited data with the following format:
	# datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
	# <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
	# hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

    data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
	print("Data Date/Time is ", data_time)

    temp = 72
    HI_TEMP = 80	# max allowable temp
	LO_TEMP = 65	# min allowable temp
	temp_alarm = "YES"
    humidity = 70
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
    
data_time, temp, HI_TEMP, LO_TEMP, temp_alarm, humidity, HI_HUMID, LO_HUMID, humidity_alarm, 
				moisture, HI_MOISTURE,LO_MOISTURE, moisture_alarm, density, HI_DENSITY, smoke_alarm, 
				fan_on, atomizer_on
	filename = "~/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"
	
	with open(filename, "a") as myfile: # appends the values, then automatically closes the file for me
    myfile.write(data_time, "\t", temp, "\t", HI_TEMP, "\t", LO_TEMP, "\t", temp_alarm, "\t", humidity, "\t", HI_HUMID, "\t", LO_HUMID, "\t",
			humidity_alarm, "\t", moisture, "\t", HI_MOISTURE, "\t", LO_MOISTURE, "\t", moisture_alarm, "\t", density, "\t",
			HI_DENSITY, "\t", smoke_alarm, "\t", fan_on, "\t", atomizer_on, "\n")
