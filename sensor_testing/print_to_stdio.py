import datetime

data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print("Data Date/Time is " + str(data_time))

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