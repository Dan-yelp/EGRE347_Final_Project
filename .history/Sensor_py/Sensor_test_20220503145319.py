import RPi.GPIO as GPIO
from time import sleep
import sys
from signal import signal, SIGINT

def handler(signal_received, frame):
    # Handle any cleanup here
    print('CTRL-C detected. Exiting from Sensor.py')
    exit(0)


def sensor_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(yellow, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)


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