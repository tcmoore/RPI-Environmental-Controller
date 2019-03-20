# Todd Moore
# 3.19.19
#!/usr/bin/env python
# coding=utf-8

# returns high & low values of temp, humidity, moisture, & density

# ************  CODE IS WORKING!!   ************
 
def hi_lo_temp(tempF, hi_temp_value, lo_temp_value):
    # hi temperature value
    if tempF > hi_temp_value:
        hi_temp_value = tempF
    # low temperature value
    if tempF < lo_temp_value:
        lo_temp_value = tempF

    return hi_temp_value, lo_temp_value

def hi_lo_humid(humidity, hi_humid_value, lo_humid_value):
   # hi humidity value
    if humidity > hi_humid_value:
        hi_humid_value = humidity
    # low humidity value
    if humidity < lo_humid_value:
        lo_humid_value = humidity
  
    return hi_humid_value, lo_humid_value

def hi_lo_moisture(moisture, hi_moisture_value, lo_moisture_value):
    # hi moisture value
    if moisture > hi_moisture_value:
        hi_moisture_value = moisture
    # low moisture value
    if moisture < lo_moisture_value:
        lo_moisture_value = moisture
 
    return hi_moisture_value, lo_moisture_value

def hi_lo_density(density, hi_density_value, lo_density_value):
     # hi density value
    if density > hi_density_value:
        hi_density_value = density
    # low moisture value
    if density < lo_density_value:
        lo_density_value = density
    
    return hi_density_value, lo_density_value


# run main() function
if __name__ == "__main__":
    # -------- Test Vectors ------------
    hi_temp_value = 0.0
    lo_temp_value = 90.0
    hi_humid_value = 0.0
    lo_humid_value = 100.0
    hi_moisture_value = 0.0
    lo_moisture_value = 1000.0
    hi_density_value = 0.0
    lo_density_value = 1000.0
    
    # Set the hi values
    tempF = 75.0
    humidity = 75.0
    moisture = 400
    density = 800
    
    hi_temp_value, lo_temp_value = hi_lo_temp(tempF, hi_temp_value, lo_temp_value)
    # print ("Hi Temp ", hi_temp_value, "Lo Temp ", lo_temp_value)
    
    hi_humid_value, lo_humid_value = hi_lo_humid(humidity, hi_humid_value, lo_humid_value)
    # print("Hi Humid ", hi_humid_value, "Lo Humid ", lo_humid_value)
    
    hi_moisture_value, lo_moisture_value = hi_lo_moisture(moisture, hi_moisture_value, lo_moisture_value)
    # print("Hi Moisture ", hi_moisture_value, "Lo Moisture ", lo_moisture_value)
    
    hi_density_value, lo_density_value = hi_lo_density(density, hi_density_value, lo_density_value)
    # print("Hi Density ", hi_density_value, "Lo Density ", lo_density_value)

    # Set the low values
    tempF = 55.0
    humidity = 55.0
    moisture = 200
    density = 600
    
    hi_temp_value, lo_temp_value = hi_lo_temp(tempF, hi_temp_value, lo_temp_value)
    # print ("Hi Temp ", hi_temp_value, "Lo Temp ", lo_temp_value)
    
    hi_humid_value, lo_humid_value = hi_lo_humid(humidity, hi_humid_value, lo_humid_value)
    # print("Hi Humid ", hi_humid_value, "Lo Humid ", lo_humid_value)
    
    hi_moisture_value, lo_moisture_value = hi_lo_moisture(moisture, hi_moisture_value, lo_moisture_value)
    # print("Hi Moisture ", hi_moisture_value, "Lo Moisture ", lo_moisture_value)
    
    hi_density_value, lo_density_value = hi_lo_density(density, hi_density_value, lo_density_value)
    # print("Hi Density ", hi_density_value, "Lo Density ", lo_density_value)

