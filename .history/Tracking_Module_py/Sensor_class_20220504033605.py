import RPi.GPIO as GPIO
from time import sleep

import sys

class Sensor:
    motion = False
    red = 24
    green = 16
    gpio_input = 4

    def sensor_init(self):
        GPIO.setwarnings(False)#The library RPi.GPIO is not optimized for real-time operations, we are updating log only once in 6 seconds.
                #Guard against some gpio problems related to erroneous mode changes
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.gpio_input, GPIO.IN)
        GPIO.output(self.red,GPIO.LOW)

    def sense_motion(self):
        GPIO.output(self.green, GPIO.HIGH)
        if GPIO.input(self.gpio_input) is 0:
            print('gpio:',GPIO.input(self.gpio_input))
            GPIO.output(self.red,GPIO.LOW)
            self.motion = False
            sleep(1)

            #sleep(6)#Accounts for delay of sensor trigger
        else:#If the GPIO-4 from sensor is high, motion is detected
            # print('Motion detected\n')
            self.motion = True
            GPIO.output(self.red,GPIO.HIGH)
            print('gpio:',GPIO.input(self.gpio_input))
            sleep(3)

            #sleep(6)#Accounts for delay of sensor trigger        
        return self.motion #Indication of motion sensor state

    def sensor_shutdown(self):
        GPIO.output(self.red,GPIO.LOW)
        GPIO.output(self.green,GPIO.LOW)
        GPIO.cleanup()