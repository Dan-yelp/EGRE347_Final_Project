import sys

sys.path.insert('/network_drive/Final_Project/EGRE347_Final_Project/EGRE347_Final_Project/Sensor_py/Sensor_class.py')

import Sensor_class
# import RPi.GPIO as GPIO
# from time import sleep
import sys
from signal import signal, SIGINT

def handler(signal_received, frame):
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
