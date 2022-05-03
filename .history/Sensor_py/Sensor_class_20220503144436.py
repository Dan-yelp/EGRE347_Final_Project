import RPi.GPIO as GPIO
from time import sleep
import sys
from signal import signal, SIGINT

class Sensor

    def Sensor():
        motion = False
        red = 24
        yellow = 5
        green = 16
        gpio_input = 4

    def handler(signal_received, frame):
        # Handle any cleanup here
        print('CTRL-C detected. Exiting from Sensor.py')
        exit(0)


    def sensor_init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(yellow, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(gpio_input, GPIO.IN)

        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(yellow, GPIO.LOW)

        GPIO.setwarnings(False)#The library RPi.GPIO is not optimized for real-time operations, we are updating log only once in 6 seconds.

    def sense_motion(self):
        red = 24
        yellow = 5
        green = 16

        gpio_input = 4

        self.motion = False

        if(GPIO.input(gpio_input)):
            print('Motion detected\n')
            motion = True
            GPIO.output(red,GPIO.HIGH)
            sleep(6)
        else:
            print('Event not detected\n')
            GPIO.output(red,GPIO.LOW)
            motion = False
        
        return motion

    def sensor_shutdown():
        GPIO.cleanup()