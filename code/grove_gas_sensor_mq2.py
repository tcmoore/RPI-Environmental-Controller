# Get air quality from Grove sensor MQ2 connected to GrovePi+ port A1


import math
import sys
import time
from grove.adc import ADC


class GroveGasSensorMQ2:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value

Grove = GroveGasSensorMQ2


def main():
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = GroveGasSensorMQ2(int(sys.argv[1]))

    print('Detecting...')
    while True:
        print('Gas value: {0}'.format(sensor.MQ2))
        time.sleep(.3)

if __name__ == '__main__':
    main()
