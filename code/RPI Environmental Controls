Raspberry Pi Environmental Controls
T.Moore
12.12.18

code that measures temp, humidity, & soil moisture, sets alarms, saves alarm data, & displays environmental data on a webpage.

Code is compatible with Python 2.7 and Python 3.5

26 usable GPIO pins on RPI Model 3 B
https://gpiozero.readthedocs.io/en/stable/


Main()
	
import datetime

# Temp Constants
TempAlarmGood 	= 	0x0001
TempAlarmHi 		= 	0x0002
	TempAlarmLo 		= 	0x0004

	# Humidity Constants
HumidAlarmGood 	= 	0x0008
HumidAlarmHi 	= 	0x0010
	HumidAlarmLo 	= 	0x0020
	
	# Soil Moisture Constants
MoistureAlarmGood 	= 	0x0040
MoistureAlarmHi 	= 	0x0080
	MoistureAlarmLo 	= 	0x0100

	# Lighting Constants
	LightOn		=	0x0200
	LightOff		=	0x0dff

#  Fan Relay Constants
	FanOn			=	0x0400
	FanOff			=	0x0bff

	# Variables
	proper_temp 		=	27		# temp should be 27 Deg C
proper_humidity	=	68		# humidity should be 68%
	proper_moisture	=	27		# soil moisture should be 77 % (??)
	TimeLightOn 		= 	5am		# what time to turn on lights
LightOnDuration 	= 	12		# how many hours until turn off lights
	CurrentTempValue 	= 	0		# measured current temp
	CurrentHumidValue 	= 	0		# measured current humidity
	CurrentMoistureValue = 	0		# measured current soil moisture
	CurrentDateTime 	= 	121218:123000	# Dec 12, 2018 12:30:00 pm
								# current system time

Main()
	While()
# --------------------------------------------------------------------
# Increment/Decrement Temp, Humidity, Soil Mixture & Light Turn On Time using
# pushbuttons
adjust_environment_variables();

# --------------------------------------------------------------------
# Get current Date, Time, Temp, Humidity, & Moisture Values
# https://tecadmin.net/get-current-date-time-python/
currentDT = datetime.datetime.now()
print (str(currentDT))
print ("Current Hour is: %d" % currentDT.hour)

CurrentTempValue 	= Get Temp		# Get temp
CurrentHumidValue 	= Get Humidity	# Get humidity
CurrentMoistureValue = Get Moisture	# Get soil moisture

# --------------------------------------------------------------------
# Check Alarms & turn on leds
check_alarms()

# --------------------------------------------------------------------
# Save History of past 24 hours
If (IsAlarm = ‘Y’) then
save_history()

# --------------------------------------------------------------------
	# display environmental values on webpage

# --------------------------------------------------------------------
	# display environmental values on OLED screen

End loop;
end;
