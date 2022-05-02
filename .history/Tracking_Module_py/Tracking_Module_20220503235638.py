import sys

import Sensor_class

import time

from signal import signal, SIGINT

import GPS_class

def handler():
    # Handle any cleanup here
    print('CTRL-C detected. Exiting from Sensor_test.py')
    exit(0)

signal(SIGINT, handler)

motion_sensor = Sensor_class.Sensor()

motion_sensor.sensor_init()

message = GPS_class.GPS()
#GPIO.setmode(GPIO.BCM)

count = 0
if len(sys.argv) < 2:
  print("Usage: <prog_name> <pty terminal path>")
  sys.exit()

try:
  pty = open(sys.argv[1], "rb")
except FileNotFoundError:
  msg = "Terminal: " + sys.argv[1] + " does not exist"
  print(msg)
  sys.exit()

print(sys.argv[1])
print("port successfully opened")

while True:
    byte = pty.read(1)
    while message.read_byte(byte) is False
        byte = pty.read(1)
    
    motion = motion_sensor.sense_motion()
    if(motion):
        print('Motion detected\n')
        time.sleep(3)

    else:
        print('No motion detected\n')
        time.sleep(3)

motion_sensor.sensor_shutdown()
