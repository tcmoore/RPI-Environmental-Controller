# Get data from Grove sensors
# Todd Moore
# 3.3.19

import grovepi

def temp()
    # Get Temperature & Humidity
	# Fahrenheit = 9.0/5.0 * Celsius + 32
	temp = (9.0/5.0 * grovepi_plus_get_temp_humidity.temp) + 32))
	humidity = grovepi_plus_get_temp_humidity.humidity
	print("Temp is: ", temp," F - Humidity is: ",humidity,"%")
	return temp, humidity

def moisture()
	# Get Soil Moisture & check if there is an alarm
	#   Here are suggested sensor values:
	#       Min  Typ  Max  Condition
	#       0    0    0    sensor in open air
	#       0    20   300  sensor in dry soil
	#       300  580  700  sensor in humid soil
	#       700  940  950  sensor in water
	moisture = grovepi_plus_get_soil_moisture.moisture
			
def air()
	# Get Air Quality Value from MQ2 sensor
	# Get sensor value
    sensor_value = grovepi.analogRead(gas_sensor)
    # Calculate gas density - large value means more dense gas
    density = (float)(sensor_value / 1024.0)
    print("sensor_value =", sensor_value, " density =", density)
    return density
 	