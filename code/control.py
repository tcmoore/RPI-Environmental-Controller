# control.py
# Todd Moore
# 3.9.19

# ******** WORKING AS OF 3.17.19 *****
# control exhaust fan, water atomizer (humidifier), & lights

from grovepi import *

def fan(temp, humidity, FAN_HI_TEMP, FAN_LO_TEMP , FAN_HI_HUMID, FAN_LO_HUMID, FAN):
    # Turn Fan on if temperature is too high or humidity is too high
    if FAN_HI_TEMP > temp > FAN_LO_TEMP:
        fan_on = "OFF"  # turn off exhaust fan led
        digitalWrite(FAN, 0)     # turn off exhaust fan   
    else:
        fan_on = "ON"   # turn on exhaust fan led
        digitalWrite(FAN, 1)     # turn on exhaust fan        
    # print("Fan is ",fan_on)
    # print("fan done")
    return fan_on

def atomizer(humidity, ATOMIZER, ATOMIZER_LO_HUMIDITY, ATOMIZER_ON_LED):
    # turn on water atomizer if humidity is too low
    if humidity <   ATOMIZER_LO_HUMIDITY:
        atomizer_on = "ON"
        digitalWrite(ATOMIZER, 1)     # turn on atomizer 
        digitalWrite(ATOMIZER_ON_LED, 1)     # turn on 'atomizer on' led
    else:
        atomizer_on = "OFF"
        digitalWrite(ATOMIZER, 0)     # turn off atomizer 
        digitalWrite(ATOMIZER_ON_LED, 0)     # turn off 'atomizer on' led
    # print("Atomizer is ", atomizer_on)
    # print("atomizer done")
    return atomizer_on

def light(light_time, LIGHT, LIGHT_START, LIGHT_STOP):
    # Turn on/off lights at a certain time
    if LIGHT_STOP > light_time > LIGHT_START:
        light_on = "ON"
        print(LIGHT_START, LIGHT_STOP, light_time)
        digitalWrite(LIGHT, 1)     # turn on grow light
    else:
        light_on = "OFF"
        digitalWrite(LIGHT, 0)     # turn off grow light
    # print("Lights are ", light_on)
    # print("light done")
    return light_on

# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    import datetime
    # -------- Test Vectors ------------
    # Hardware constants
    ATOMIZER_ON_LED = 5
    ATOMIZER = 7
    LIGHT = 16  # uses A2 as digital channels 16 & 17
    FAN = 17    # uses A2 as digital channels 16 & 17

    pinMode(LIGHT,"OUTPUT")
    pinMode(FAN,"OUTPUT")
    pinMode(ATOMIZER,"OUTPUT")
    pinMode(ATOMIZER_ON_LED,"OUTPUT")
    time.sleep(1)
    
    #Software constants
    FAN_HI_TEMP = 80    # max allowable temp
    FAN_LO_TEMP = 65    # min allowable temp
    FAN_HI_HUMID = 85   # max allowable humidity percentage
    FAN_LO_HUMID = 65   # min allowable humidity percentage
    FAN_HI_MOISTURE = 700   # max allowable soil moisture level
    ATOMIZER_LO_HUMIDITY = 65   # humidity level water atomizer turns on
    LIGHT_START = '15:00'
    LIGHT_STOP = '16:00'
    temp = 75
    humidity = 75
    light_time = datetime.datetime.now().strftime("%H:%M")
    print("Fan Hi Temp, & Fan Low Temp Vectors are: ", FAN_HI_TEMP, FAN_LO_TEMP)
    print("Fan High Humid, & Fan Low Humid Vectors are: ", FAN_HI_HUMID, FAN_LO_HUMID)
    print("Temp & Humidity Vectors are: ", temp, humidity)
    fan(temp, humidity, FAN_HI_TEMP, FAN_LO_TEMP , FAN_HI_HUMID, FAN_LO_HUMID, FAN)
    print("Humidity & Atomizer Low Humidity Vectors are: ", humidity, ATOMIZER_LO_HUMIDITY)
    atomizer(humidity, ATOMIZER, ATOMIZER_LO_HUMIDITY, ATOMIZER_ON_LED)
    print("Light Date/Time is ", light_time)
    print("Light Start Time & Stop time is: ", LIGHT_START, LIGHT_STOP)
    light(light_time, LIGHT, LIGHT_START, LIGHT_STOP)
 