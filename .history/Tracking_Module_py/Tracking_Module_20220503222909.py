import sys

import Sensor_class

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
        print('Motion\n')
    else:
        print('No motion\n')

motion_sensor.sensor_shutdown()
