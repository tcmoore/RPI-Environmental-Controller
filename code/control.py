# control hardware connected to RPI
# Todd Moore
# 3.4.19

import grovepi

	def fan(temp, humidity,fan)
        # --------------------------------------------------------------------
		# Turn Fan on if temperature is too high or humidity is too high
		if temp > 77 or humidity > 80:
			fan_on = "ON"
			grovepi.digitalWrite(fan,1)     # turn on exhaust fan	
		else:
			fan_on = "OFF"
			grovepi.digitalWrite(fan,0)     # turn off exhaust fan		
		print("Fan is ",fan_on)
		return fan_on

    def atomizer(humidity, atomizer)	
		# --------------------------------------------------------------------
		# turn on water atomizer if humidity is too low
		if humidity < 40:
			atomizer_on = "ON"
			grovepi.digitalWrite(atomizer,1)     # turn on humidity alarm led		
		else:
			atomizer_on = "OFF"
			grovepi.digitalWrite(atomizer,0)     # turn off humidity alarm led		
		print("Atomizer is ", atomizer_on)
        return atomizer_on

	def light(light_time, light,light_start, light_stop)
		# Turn on/off lights @ a certain time.
		if lights_time = light_start:
			light_on = "ON"
			grovepi.digitalWrite(light,1)     # turn on grow light @ 5AM
		if lights_time = light_stop:
			light_on = "OFF"
			grovepi.digitalWrite(light,0)     # turn off grow light @ 5PM
		return light_on