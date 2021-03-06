import sys

import Sensor_class

import time

from signal import signal, SIGINT

def handler():
    # Handle any cleanup here
    print('CTRL-C detected. Exiting from Sensor_test.py')
    exit(0)

signal(SIGINT, handler)

motion_sensor = Sensor_class.Sensor()

motion_sensor.sensor_init()

while(1):
    motion = motion_sensor.sense_motion()
    if(motion):
        print('Motion detected\n')
        time.sleep(3)

    else:
        print('No motion detected\n')

motion_sensor.sensor_shutdown()
