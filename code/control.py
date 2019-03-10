# control.py
# Todd Moore
# 3.9.19

# control exhaust fan, water atomizer (humidifier), & lights

# import grovepi

def fan(temp, humidity, FAN_HI_TEMP, FAN_LOW_TEMP , FAN_HI_HUMID, FAN_LO_HUMID, FAN):
	# Turn Fan on if temperature is too high or humidity is too high
	if FAN_HI_TEMP > temp > FAN_LO_TEMP:
		fan_on = "OFF"	# turn off exhaust fan led
		# grovepi.digitalWrite(FAN, 0)     # turn off exhaust fan	
	else:
		fan_on = "ON"	# turn on exhaust fan led
		# grovepi.digitalWrite(FAN, 1)     # turn on exhaust fan		
	print("Fan is ",fan_on)
	print("fan done")
	return fan_on

def atomizer(humidity, ATOMIZER):
	# turn on water atomizer if humidity is too low
	if humidity < 	ATOMIZER_LO_HUMIDITY:
		atomizer_on = "ON"
		# grovepi.digitalWrite(ATOMIZER,1)     # turn on humidity alarm led		
	else:
		atomizer_on = "OFF"
		# grovepi.digitalWrite(ATOMIZER,0)     # turn off humidity alarm led		
	print("Atomizer is ", atomizer_on)
	print("atomizer done")
	return atomizer_on

def light(light_time, LIGHT, LIGHT_START, LIGHT_STOP):
	# Turn on/off lights at a certain time
	if LIGHT_STOP > light_time > LIGHT_START:
		light_on = "ON"
		print(LIGHT_START, LIGHT_STOP, light_time)
		# grovepi.digitalWrite(LIGHT, 1)     # turn on grow light
	else:
		light_on = "OFF"
		# grovepi.digitalWrite(LIGHT, 0)     # turn off grow light
	print("Lights are ", light_on)
	print("light done")
	return light_on

# run main() function
if __name__ == "__main__":
	print("Executing as main program")
	print("Value of __name__ is: ", __name__)
	import datetime
	# -------- Test Vectors ------------
	# Hardware constants
	ATOMIZER = 3
	LIGHT = 4
	FAN = 5
	#Software constants
	FAN_HI_TEMP = 80	# max allowable temp
	FAN_LO_TEMP = 65	# min allowable temp
	FAN_HI_HUMID = 85	# max allowable humidity percentage
	FAN_LO_HUMID = 65	# min allowable humidity percentage
	FAN_HI_MOISTURE = 700	# max allowable soil moisture level
	ATOMIZER_LO_HUMIDITY = 65	# humidity level water atomizer turns on
	LIGHT_START = '15:00'
	LIGHT_STOP = '17:00'
	temp = 72
	humidity = 64
	light_time = datetime.datetime.now().strftime("%H:%M")
	print("Fan Hi Temp, & Fan Low Temp Vectors are: ", FAN_HI_TEMP, FAN_LO_TEMP)
	print("Fan High Humid, & Fan Low Humid Vectors are: ", FAN_HI_HUMID, FAN_LO_HUMID)
	print("Temp & Humidity Vectors are: ", temp, humidity)
	fan(temp, humidity, FAN_HI_TEMP, FAN_LO_TEMP , FAN_HI_HUMID, FAN_LO_HUMID, FAN)
	print("Humidity & Atomizer Low Humidity Vectors are: ", humidity, ATOMIZER_LO_HUMIDITY)
	atomizer(humidity, ATOMIZER, ATOMIZER_LO_HUMIDITY)
	print("Light Date/Time is ", light_time)
	print("Light Start Time & Stop time is: ", LIGHT_START, LIGHT_STOP)
	light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)
	