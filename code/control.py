# control hardware connected to RPI
# Todd Moore
# 3.4.19

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