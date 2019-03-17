# Raspberry Pi Environmental Controls For My Growbox Design
# Todd Moore
# 12.22.18

#!/usr/bin/env python
# coding=utf-8
# # code that measures temp, humidity, & soil moisture, sets alarms, saves alarm data, increases humidity in growbox,
# & displays environmental data on an RGB LCD & webpage.

# Code is compatible with Python 2.7 and Python 3.5.

# Code is for Raspberry Pi with the GrovePi+ hat attached to the GPIO connector.

# RPI/Grove Pinout Definitions
# Port#     Pin on Port#    Type            Sensor/Module
# ---------------------------------------------------------------
# SERIAL    D0      DIGITAL & SERIAL    Grove Buzzer
# D2    D2      DIGITAL         Grove - Temperature&Humidity Sensor Pro
# D3    D3      DIGITAL         Grove - Water Atomization
#               Grove - 2-Channel SPDT Switch 1 (Bottom Connector) - Exhaust Fan
#                               Grove 2-Channel SPDT Switch 1 (Bottom Connector) Exhaust Fan

import datetime
#import grovepi
#import setup_rpi
#import get
#import check_alarms
#import control
#import send_values
#import grove_rgb_lcd

#def foo():
    # define the main() function
    # while True:
    #     try:
    #         # ----------------------------------------    
    #         # Get current date & time
    #         data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
    #         print("Data Date/Time is ", data_time)

# run main() function
#if __name__ == "__main__":
# foo()

# from check_alarms.py


foo = 100

def hello():
    print("i am from my_module.py")
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
    print("Data Date/Time is ", data_time)

if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello()
   