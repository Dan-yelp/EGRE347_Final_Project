import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)#The library RPi.GPIO is not optimized for real-time operations

red = 24
yellow = 5
green = 16

gpio_input = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(gpio_input, GPIO.IN)

GPIO.output(red, GPIO.HIGH)
GPIO.output(green, GPIO.HIGH)
GPIO.output(yellow, GPIO.HIGH)

for y in range(1,24):
    # GPIO.setup(y, GPIO.OUT)
    GPIO.output(red,GPIO.LOW)
    sleep(1)
    print('they should be high\n')
    GPIO.output(red,GPIO.HIGH)
    sleep(1)

for x in range(10000):
    if(GPIO.event_detected(gpio_input)):
        print('Event detected\n')
        GPIO.output(red,GPIO.HIGH)
    else:
        print('Event not detected\n')
        GPIO.output(red,GPIO.LOW)
    sleep(1)
#Option 1, the program waits for the sensor to cause a falling edge to do anything
#GPIO.wait_for_edge(gpio_input, GPIO.FALLING) #This would be a good way to trigger the event

#Option 2, continuously poll GPS location, trigger the event like this
# GPIO.add_event_detect(gpio_input, GPIO.FALLING)

# if(GPIO.event_detected(gpio_input)):
#     print('Event _detected\n')