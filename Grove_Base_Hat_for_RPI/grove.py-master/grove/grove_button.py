#!/usr/bin/env python
#
# This library is for Grove - Button(https://www.seeedstudio.com/s/Grove-Button-p-766.html)
#
# This is the library for Grove Base Hat which used to connect grove sensors for raspberry pi.
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
import time
from grove.button import Button
from grove.factory import Factory


class GroveButton(object):
    def __init__(self, pin):
        # High = pressed
        self.__btn = Factory.getButton("GPIO-HIGH", pin)
        self.__last_time = time.time()
        self.__on_press = None
        self.__on_release = None
        self.__btn.on_event(self, GroveButton.__handle_event)

    @property
    def on_press(self):
        return self.__on_press

    @on_press.setter
    def on_press(self, callback):
        if not callable(callback):
            return
        self.__on_press = callback

    @property
    def on_release(self):
        return self.__on_release

    @on_release.setter
    def on_release(self, callback):
        if not callable(callback):
            return
        self.__on_release = callback

    def __handle_event(self, evt):
        dt, self.__last_time = evt["time"] - self.__last_time, evt["time"]
        # print("event index:{} event:{} pressed:{}".format(evt["index"], evt["code"], evt["pressed"]))
        if evt["code"] == Button.EV_LEVEL_CHANGED:
            if evt["pressed"]:
                if callable(self.__on_press):
                    self.__on_press(dt)
            else:
                if callable(self.__on_release):
                    self.__on_release(dt)


Grove = GroveButton

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()

    button = GroveButton(pin)

    def on_press(t):
        print('Button is pressed')
    def on_release(t):
        print("Button is released, pressed for {0} seconds".format(round(t,6)))

    button.on_press = on_press
    button.on_release = on_release

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
