import RPi.GPIO as GPIO
from time import sleep
import sys
from signal import signal, SIGINT
import Sensor_class

def handler(signal_received, frame):
    # Handle any cleanup here
    print('CTRL-C detected. Exiting from Sensor.py')
    exit(0)

signal(SIGINT, handler)

motion_sensor = Sensor_class.Sensor()

motion_sensor.sensor_init()

while(1):
    motion_sensor.sense_motion()
motion_sensor.sensor_shutdown()