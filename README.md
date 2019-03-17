# RPI-Environmental-Controller

**** TESTING CALLING FUNCTIONS FROM WITHIN MAIN CODE, USING PYTHON FILES FOR EACH FUNCTION  ****
**** MASTER BRANCH USES NO PYTHON FILES & DOES ALL THE WORK IN THE MAIN CODE  ****

This is my design of a Raspberry PI B Environmental Controller. It will be used in a 2'x2'x6' grow box.  This design will have many stages until completion.  Check documentation on this github repository for detailed descriptions of the design.

Design goals are:
- Read Temp (temp/humidity sensor)
- Read Humidity (temp/humidity sensor)
- Read Soil Moisture (soil moisture sensor)
- Read air quality for smoke (are quality sensor)
- Visual alarms for over/under values of temp/humidity/soil moisture (leds)
- Alarm with sound if smoke is detected (buzzer)

Icing on the cake would be:
- Visual Display (LCD Display)
- Increase humidity in grow box if humidity is too low (water atomizer)
- Interactive controls for changing env values (buttons)
- IoT/Web page access/control
- Push alarms to me via text/email
- Add water to soil based on soil moisture value (relay, water pump)
- Turn grow lights on/off using RPI (relay)
- Turn on/off fan based on temp & humidity using RPI (relay)

- MY DESIGN DOCUMENT USING GROVE COMPONENTS
  - https://github.com/tcmoore/RPI-Environmental-Controller/blob/master/RPI%20Environmental%20Control%20Project.pdf
  
- MY DESIGN DIAGRAM SHOWING WHERE THE GROVE SENSORS & MODULES & LEDS WILL BE CONNECTED TO THE GROVEPI PLUS HAT
  - https://github.com/tcmoore/RPI-Environmental-Controller/blob/master/GrovePi_Plus_Hat_Sensor%20to%20Pin%20List.pdf\
  
- MY CODE
  - https://github.com/tcmoore/RPI-Environmental-Controller/tree/master/code
__________________________________________________________________________________________________________________________

Websites for reference:

- RPI DOCS
  - https://www.raspberrypi.org/documentation/usage/python/
  - https://github.com/raspberrypi

- RPI GPIO PINOUT
  - https://pinout.xyz/
  
- Tkinter GUI Widgets Code
  - https://www.dummies.com/programming/python/using-tkinter-widgets-in-python/

- Other GUI Libraries/Code
  - https://insights.dice.com/2017/08/07/7-top-python-gui-frameworks-for-2017-2/
  - https://wiki.python.org/moin/WebFrameworks/
  
- GPIO
  - https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
  - http://www.thirdeyevis.com/pi-page-2.php  - GPIO LED
  
- FILES
  - https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
  
- DATE/TIME
  - https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
  - https://raspberrypi.stackexchange.com/questions/37802/turn-led-on-after-a-particular-time-for-a-particular-time-period#37807
    
- EMAIL
  - http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email

- GROVE SENSOR GITHUB LIBRARY
  - https://github.com/DexterInd/GrovePi
  
- Example Projects
  - https://www.cyber-omelette.com/2017/09/automated-plant-watering.html
  
- IOT Using Android Phone
  - Blynk
  - https://www.blynk.cc/
  - https://github.com/vshymanskyy/blynk-library-python
  - https://www.pibakery.org/
  - https://github.com/blynkkk/blynk-server#quick-local-server-setup-on-raspberry-pi    - install local Blynk server on RPI
  - https://github.com/switchdoclabs/SDL_Pi_SmartGardenSystem                           - garden system python code using Blynk

- Running Ardiuno Sketches C++ (Programs) on RPI using the Arduino IDE installed on local computer.
 - Compile C++ sketches in Arduino on local computer as a binary file that can be copied to the RPI and ran using $ sudo ./sketch.bin
 
 - https://www.youtube.com/watch?v=lZvhtfUlY8Y
 
- Using Free Visual Studio Code IDE with github
  - https://code.visualstudio.com//#built-in-git
  - https://code.visualstudio.com/docs/editor/versioncontrol
  - https://youtu.be/wMqukSKYcvU                    - Video showing how to use git in Vstudio Code
  - https://www.youtube.com/watch?v=c3482qAzZLQ     - Not using free version of Vstudio, but good git
                                                        command-line ref anyway

- PEP 8 -- Style Guide for Python Code
  - https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces
  
__________________________________________________________________________________________________________________________

License
This project is released under The MIT License (MIT)

Copyright 2019 Todd Moore

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
  
  
