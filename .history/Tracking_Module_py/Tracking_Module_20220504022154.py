import sys

import Sensor_class

import time

from signal import signal, SIGINT

import GPS_class

        # print('Motion detected\n')
# python 3 script to take a picture with the Pi camera
# and take a histogram of it. Bothe the original image
# and the histogram are saved as .jpg files
#
# Author: Peter Truslow 27 March, 2020

# import packages needed by the program
import time
import picamera
import picamera.array
import cv2
import matplotlib

# command to allow using matplotlib on a headless Pi
matplotlib.use('Agg')

# use the matplotlib library to plot our histogram as an image
from matplotlib import pyplot 

def handler(SIGINT, handler):
    # Handle any cleanup here
    motion_sensor.shutdown()
    print('CTRL-C detected. Exiting Tracking_Module.py safely.\n')
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

count = 0 #keeps track of how many images were saved
while True:
    motion = motion_sensor.sense_motion()
    # time.sleep(2)
    
    if(motion):
        byte = pty.read(1)
        while message.read_byte(byte) is False:
            byte = pty.read(1)

        with picamera.PiCamera() as camera:
            # start the camera early so it can adjust to lighting
            camera.start_preview()
            # wait 2 seconds
            time.sleep(2)
            with picamera.array.PiRGBArray(camera) as stream:
                # opencv uses bgr order for some reason
                camera.capture(stream, format='bgr')
                # At this point the image is available as stream.array
                # access image as a NumPy array
                image = stream.array
                # save original image
                print('Saving Image\n')
                temp_str = str()
                temp_str = 'image'+str(count)
                temp_str = temp_str + '.jpg'
                
                cv2.imwrite(temp_str, image)
                #generate 1-D histogram
                # hist = cv2.calcHist([image],[0],None,[256],[0,256])
                # plot histogram with intensity on x axis, 
                # number of pixels at each intensity along y
                # pyplot.plot(hist)
                # #save histogram as jpg
                # pyplot.savefig('histogram.jpg')
                # #save log here
                time.sleep(2)

    # else:
    #     print('No motion detected\n')
        # time.sleep(3)

motion_sensor.sensor_shutdown()
