# Get data from Grove sensors
# Todd Moore
# 3.3.19

import grovepi
import time

def temp(TEMP_SENSOR, WHITE):
    try:
        # Get Temperature & Humidity
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(TEMP_SENSOR,WHITE) 
        # Convert to Fahrenheit = 9.0/5.0 * Celsius + 32
        tempF = (9.0/5.0 * temp) + 32
        print("Temp/Humidity is: ", temp, humidity)
        print("get.temp module done")
        return tempF, humidity

    except IOError:
        print ("Temp/Humid Sensor Error")

def moisture(MOISTURE_SENSOR):
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water

    #   Sensor values observer: 
    #       Values  Condition
    #       --------------------------
    #       0-17    sensor in open air
    #       18-424  sensor in dry soil
    #       425-689 sensor in humid soil
    #       690+    sensor in water
    try:
        moisture_level = grovepi.analogRead(MOISTURE_SENSOR)
        print("get.moisture module done")
        return moisture_level

    except IOError:
        print ("Moisture Sensor Error")
            
def air(GAS_SENSOR):
    # MQ2 - Combustible Gas, Smoke
    # The sensitivity can be adjusted by the onboard potentiometer
    try:
        # Get Air Quality Value from MQ2 sensor
        # Get sensor value
        sensor_value = grovepi.analogRead(GAS_SENSOR)
        # Calculate gas density - large value means more dense gas
        density = (float)(sensor_value / 1024.0)
        print("sensor_value =", sensor_value, " density =", density)
        print("get.density done")
        return density
    
    except IOError:
        print ("Moisture Sensor Error")



# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    
    # -------- Test Vectors ------------
    # Hardware constants
    GAS_SENSOR = 0  # Connect MQ2 to Analog port A0, pin 0
    MOISTURE_SENSOR = 2 # Analog port A2, pin 2
    TEMP_SENSOR = 2 # Digital pin D2, pin 2

    #Software constants
    WHITE = 1  # The Temp Sensor covor color is white.
    
    tempF, humidity = temp(TEMP_SENSOR, WHITE)
    moisture_level = moisture(MOISTURE_SENSOR)  
    density = air(GAS_SENSOR)   
    print("Temp is: ", tempF," F - Humidity is: ",humidity,"%")
    print("Soil Moisture is: ", moisture_level)
    print("Density is: ", density)
