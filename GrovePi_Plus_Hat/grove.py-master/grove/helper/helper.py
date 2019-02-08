#!/usr/bin/env python
#
# This is the library for Grove Base Hat.
#
# Helper Classes
#

'''
## License

The MIT License (MIT)

Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
Copyright (C) 2018  Seeed Technology Co.,Ltd. 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from __future__ import print_function
from grove.adc import *
import time
import sys
import os
import re

_SlotsGPIORpi     = { 5:"D5", 12:"PWM", 16:"D16", 18:"D18", 22:"D22", 24:"D24", 26:"D26" }
_SlotsGPIORpiZero = { 5:"D5", 12:"PWM", 16:"D16"           }
_SlotsADCRpi      = { 0:"A0",  2:"A2",   4:"A4",   6:"A6"  }
_SlotsADCRpiZero  = { 0:"A0",  2:"A2",   4:"A4"            }
_SlotsPWMRpi      = {         12:"PWM",           18:"D18" }
_SlotsPWMRpiZero  = {         12:"PWM"                     }
_SlotsNull        = { }

class SlotHelper(object):
    # Slot types
    GPIO = 0
    ADC  = 1
    PWM  = 2
    I2C  = 3
    UART = 4

    def __init__(self, slot):
        adc = ADC()
        name = adc.name
        print("Hat Name = '{}'".format(name))
        if name == RPI_ZERO_HAT_NAME:
            self.__hat_type = RPI_ZERO_HAT_PID
            self.__slots_gpio = _SlotsGPIORpiZero
            self.__slots_adc  = _SlotsADCRpiZero
            self.__slots_pwm  = _SlotsPWMRpiZero
        elif name != RPI_HAT_NAME:
            print("Unknown hat, assume {}".format(RPI_HAT_NAME))
        if name != RPI_ZERO_HAT_NAME:
            self.__hat_type = RPI_HAT_PID
            self.__slots_gpio = _SlotsGPIORpi
            self.__slots_adc  = _SlotsADCRpi
            self.__slots_pwm  = _SlotsPWMRpi
        self.__slots_i2c = _SlotsNull
        maps = {                       \
                SlotHelper.GPIO:self.__slots_gpio, \
                SlotHelper.ADC :self.__slots_adc,  \
                SlotHelper.PWM :self.__slots_pwm,  \
                SlotHelper.I2C :self.__slots_i2c,  \
                }

        self._slots = maps.get(slot)
        self._slot  = slot

    def is_adapted(self, pin):
        if not self._slots:
            return False
        if not pin in self._slots.keys():
            return False
        return True

    def list_avail(self):
        if not self._slots:
            return

        maps = {                          \
                SlotHelper.GPIO: "GPIO",  \
                SlotHelper.ADC : "ADC",   \
                SlotHelper.PWM : "PWM",   \
                SlotHelper.I2C : "I2C",   \
                }

        print(" <pin> could be one of below values")
        print("       in the pin column for {} function".format(maps.get(self._slot)))
        print("   And connect the device to corresponding slot")
        print("==============")
        print(" pin | slot")
        print("==============")
        for pin, slot in self._slots.items():
            print('{:^5}|{:^5} '.format(pin, slot))

    def argv2pin(self, extra=''):
        if len(sys.argv) < 2:
            usage = 'Usage: {} <pin>'.format(sys.argv[0])
            usage += extra
            print(usage)
            self.list_avail()
            sys.exit(1)

        pin = int(sys.argv[1])
        if not self.is_adapted(pin):
            self.list_avail()
            sys.exit(1)
        return pin

def root_check():
    if os.geteuid() != 0:
        print("This program must be run as root.")
        print("sudo required for non-root user, Aborting.")
        sys.exit(1)

def __module_installed(name):
    for line in os.popen("lsmod"):
        match = re.match("^" + name + " *", line)
        if match is None: continue
        # print("result = {}".format(match))
        return True
    return False

def module_install(name, param):
    if __module_installed(name):
        return True
    os.system("modprobe " + name + " " + param)
    for _ in range(20):
        if __module_installed(name):
            return True
        time.sleep(0.2)
    return False


class OverlayHelper(object):
    def __init__(self, dev_path, overlay, param):
        self._path = dev_path
        self._ovlay = overlay
        self._param = param

    def __is_dt_inst(self):
        for line in os.popen("dtoverlay -l"):
            # lines likes
            #2:  w1-gpio  gpiopin=5
            match = re.match("^[0-9]+: *" + self._ovlay + " +", line)
            if match is None: continue
            return True
        return False

    def is_installed(self):
        if os.path.exists(self._path):
            return True
        if self.__is_dt_inst():
            return True
        return False

    def install(self):
        if self.is_installed():
            return True
        os.system("dtoverlay " + self._ovlay + " " + self._param)
        for _ in range(20):
            if self.is_installed():
                return True
            time.sleep(0.2)
        return False

    def __str__(self):
        return "Overlay {} installed = {}".format(
               self._ovlay, self.is_installed())

    # __repr__ = __str__

    @property
    def name(self):
        return self._ovlay


if __name__ == '__main__':
    print("module w1_therm installed: {}"
          .format(__module_installed("w1_therm")))
    module_install("w1_therm", "")
    print("module w1_therm installed: {}"
          .format(__module_installed("w1_therm")))
    print("module w1_gpio  installed: {}"
          .format(__module_installed("w1_gpio")))
    oh = OverlayHelper("/sys/devices/w1_bus_master1",
                       "w1-gpio",
                       "gpiopin=5")
    print(oh)
    print("install {} ...".format(oh.name))
    oh.install()
    print(oh)

