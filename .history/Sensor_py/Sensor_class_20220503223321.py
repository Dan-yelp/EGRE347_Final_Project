import RPi.GPIO as GPIO
from time import sleep
import sys

class Sensor:
    motion = False
    red = 24
    yellow = 5
    green = 16
    gpio_input = 4

    def sensor_init(self):
        GPIO.setwarnings(False)#The library RPi.GPIO is not optimized for real-time operations, we are updating log only once in 6 seconds.
                #Guard against some gpio problems related to erroneous mode changes
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.gpio_input, GPIO.IN)

    def sense_motion(self):

        self.motion = False

        if not GPIO.input(self.gpio_input):
            # print('Event not detected\n')
            GPIO.output(self.red,GPIO.LOW)
            self.motion = False
            #sleep(1)

            #sleep(6)#Accounts for delay of sensor trigger
        else:#If the GPIO-7 from sensor is high, motion is detected
            # print('Motion detected\n')
            self.motion = True
            GPIO.output(self.red,GPIO.HIGH)

            #sleep(6)#Accounts for delay of sensor trigger        
        return self.motion #Indication of motion sensor state

    def sensor_shutdown():
        GPIO.output(self.red,GPIO.LOW)
        GPIO.output(self.red,GPIO.LOW)
        GPIO.output(self.red,GPIO.LOW)
        GPIO.cleanup()