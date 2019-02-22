# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 12.22.18

# code that measures temp, humidity, & soil moisture, sets alarms, saves alarm data, increases humidity in growbox,
# & displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
#	Port# 	Pin on Port# 	Type			Sensor/Module
#	---------------------------------------------------------------
#	SERIAL	D0	 	DIGITAL & SERIAL	Grove Buzzer
#	D2 	D2	 	DIGITAL 		Grove - Temperature&Humidity Sensor Pro
#	D3 	D3	 	DIGITAL 		Grove - Water Atomization
#	D4 	D4 & D5 	DIGITAL 		Grove - 2-Channel SPDT Switch 1 (Top Connector) – LED Lights
#							Grove - 2-Channel SPDT Switch 1 (Bottom Connector) – Exhaust Fan
#	D5 	D5 & D6 	DIGITAL 		-
#	D6 	D6	 	DIGITAL 		Temp Alarm LED
#	D7 	D7	 	DIGITAL 		Humid Alarm LED
#	D8 	D8	 	DIGITAL 		Moisture Alarm LED
#	A0 	A0 & A1 	ANALOG 			-
#	A1 	A1	 	ANALOG			Grove MQ2 Air Sensor
#	A2	A2 		ANALOG 			Grove - Moisture Sensor
#	I2C-1 			I2C -
#	I2C-2 			I2C -
#	I2C-3 			I2C 			Grove - LCD RGB Backlight
#	RPRISER 		RPI SERIAL

def main()
	# define the main() function
	# ...
	
# run main() function
if __name__ == "__main__":
    main()


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
