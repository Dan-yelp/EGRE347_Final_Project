import Sensor_class
import sys
from signal import signal, SIGINT


def handler(signal_received, frame):
    # Handle any cleanup here
    print('CTRL-C detected. Exiting from Sensor.py')
    exit(0)


motion_sensor = Sensor_class.Sensor()

motion_sensor.sensor_init()

while(1):
    motion_sensor.sense_motion()
motion_sensor.sensor_shutdown()