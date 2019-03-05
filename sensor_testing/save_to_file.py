

import datetime

# Values will be added as tab seperated delimited data with the following format:
# datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
# <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
# hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
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
  	
filename = "/home/pi/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"

# concatenate data into 1 string argument
values = data_time + "\t" + str(temp) + "\t" + str(HI_TEMP) + "\t" + str(LO_TEMP) + "\t" + humid_alarm + "\t"\
    + str(moisture) + "\t" + str(HI_MOISTURE) + "\t", str(LO_MOISTURE) + "\t" + moisture_alarm + "\t" + str(density) + "\t"\
    + str(HI_DENSITY) + "\t" + smoke_alarm + "\t" + fan_on + "\t" + atomizer_on + "\n"

print(values)

# appends the values, then automatically closes the file for me
with open(filename, "a") as myfile: 
    myfile.writelines(values)
