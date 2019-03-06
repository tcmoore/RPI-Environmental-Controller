# read from file reads a line of data from a file
# Todd Moore
# 3.6.19
 	
# Values in the file are tab seperated delimited data with the following format:
# datetime <TAB> temp <TAB> hi temp <TAB> low temp <TAB> temp_alarm <TAB> humidity <TAB> hi humidity <TAB> low humidity
# <TAB> humidity alarm <TAB> moisture <TAB> hi moisture <TAB> low moisture <TAB> moisture alarm <TAB> density <TAB>
# hi density <TAB> smoke alarm <TAB> fan on <TAB> ataomizer on \n

filename = "/home/pi/RPI-Environmental-Controller/testingV1-Branch/RPI-Environmental-Controller/values.txt"


# reads the line of values, then automatically closes the file for me
with open(filename) as fp:
    lines = fp.readlines()
print(lines)