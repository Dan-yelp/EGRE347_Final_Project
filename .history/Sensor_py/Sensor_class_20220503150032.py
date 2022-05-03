import RPi.GPIO as GPIO
from time import sleep
import sys
from signal import signal, SIGINT

class Sensor:
    motion = False
    red = 24
    yellow = 5
    green = 16
    gpio_input = 4

    def Sensor():
        motion = False
        red = 24
        yellow = 5
        green = 16
        gpio_input = 4

    def sensor_init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.gpio_input, GPIO.IN)

        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.yellow, GPIO.HIGH)

        GPIO.setwarnings(False)#The library RPi.GPIO is not optimized for real-time operations, we are updating log only once in 6 seconds.
        sleep(5)
    def sense_motion(self):
        self.motion = False
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.gpio_input, GPIO.IN)

        if(GPIO.input(self.gpio_input)):
            print('Motion detected\n')
            self.motion = True
            GPIO.output(self.red,GPIO.HIGH)
            sleep(6)
        else:
            print('Event not detected\n')
            GPIO.output(self.red,GPIO.LOW)
            self.motion = False
        
        return self.motion

    def sensor_shutdown():
        GPIO.cleanup()