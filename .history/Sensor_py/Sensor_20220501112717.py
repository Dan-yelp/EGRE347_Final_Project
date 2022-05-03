import RPi.GPIO as GPIO

red = 24
yellow = 5
green = 16

gpio_input = 17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(gpio_input, GPIO.IN)

GPIO.output(red, GPIO.HIGH)
GPIO.output(green, GPIO.HIGH)
GPIO.output(yellow, GPIO.HIGH)

#Option 1, the program waits for the sensor to cause a falling edge to do anything
GPIO.wait_for_edge(gpio_input, GPIO.FALLING) #This would be a good way to trigger the event

#Option 2, continuously poll GPS location, trigger the event like this
GPIO.add_event_detect(gpio_input, GPIO.FALLING)

if(GPIO.event_detected(gpio_input))