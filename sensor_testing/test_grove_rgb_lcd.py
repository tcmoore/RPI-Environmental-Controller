# Raspberry Pi Grove I2C RGB LCD Backlight Testing
# Todd Moore
# 2.27.19

# Code is compatible with Python 2.7 and Python 3.5.

# Testing Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

import grovepi
import grove_rgb_lcd

def main()
  # --------------------------------------------------------------------
	# Display Environmental Data on LCD Screen
  setRGB(0,128,64)
  time.sleep(2)
	setText("Date/Time: ", now.strftime("%Y-%m-%d %I:%M"))
  time.sleep(5)
						
# run main() function
if __name__ == "__main__":
    main()
