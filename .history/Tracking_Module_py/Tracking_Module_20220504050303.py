#******************************************************************
# Program #: Sensing thermal motion, and logging data.
#
# Programmer: Daniel Jordan Youngk, Mehmet Kutlug
#
# Due Date: NA
#
# EGRE 347, Spring 2022       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python example for reading information from serial port one byte at a time
#
# Input: GPIO Pin 4 (Input from sensor), time and location data from GPS dongle.
#
# Output: location_log.csv which contains comma delimited values one column at a time
#         image<n>.jpg image that matches filename in location_log.csv
#         *Location and image are stored when motion is sensed.
#
#******************************************************************

#External modules discussed in curriculum
import sys
import Sensor_class
from time import sleep
from signal import signal, SIGINT
import GPS_class


# python 3 script to take a picture with the Pi camera
# and take a histogram of it. Bothe the original image
# and the histogram are saved as .jpg files
#
# Author: Peter Truslow 27 March, 2020
# import packages needed by the camera program
import time
import picamera
import picamera.array
import cv2
import matplotlib

# command to allow using matplotlib on a headless Pi
matplotlib.use('Agg')

# use the matplotlib library to plot our histogram as an image
from matplotlib import pyplot 

#Handles log filing
import os

#Allows user to ctrl+c to exit program safely
def handler(SIGINT, handler):
    # Clean up GPIO board
    motion_sensor.sensor_shutdown()
    print('\nCTRL-C detected. Exiting Tracking_Module.py safely.\n')
    exit(0)

#Enables handler interrupt
signal(SIGINT, handler)

#Options for programmer
#Output file format
output_filename = 'location_log.csv'

if os.path.exists(output_filename):
    os.remove(output_filename)

n = int(0)
#filename[n], where n is the index of the image
image_filename = 'buffer_image'

while(os.path.exists(image_filename+'['+ str(n) + '].jpg')):
    os.remove(image_filename+'['+ str(n) + '].jpg')
    image_filename = image_filename + '['+ str(n) + '].jpg'
    n = n + 1
    print("Removing buffer image:", image_filename)

#Used to interface sensor
motion_sensor = Sensor_class.Sensor()
motion_sensor.sensor_init()

#Class structure holding information about data being received, and methods for processing new data
message = GPS_class.GPS()


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
print("port with G-mouse successfully opened")

#keeps track of how many images get saved
count = 0 

#Sparce GPS messages, poll the motion sensor as often as possible given physical 
#constraints, and process tagged instances 
while True:
    motion = motion_sensor.sense_motion()
    print("Value of motion:", motion,"\n")
    #If motion is sensed, tag next available location
    if(motion):
        #Reading data one byte at a time from terminal with (G-mouse)
        byte = pty.read(1)
        while message.read_byte(byte) is False:
            byte = pty.read(1)

        print("Creating buffer image\n")
        #New full message: image filename, time, longitude, and latitude
        with picamera.PiCamera() as camera:
            # start the camera early so it can adjust to lighting
            camera.start_preview()
            # wait 2 seconds
            time.sleep(2)
            with picamera.array.PiRGBArray(camera) as stream:
                # opencv uses bgr order for some reason
                camera.capture(stream, format='rgb')
                # At this point the image is available as stream.array
                # access image as a NumPy array
                image = stream.array
                # save image
                # print('Saving Image\n')
                count = count + 1
                
                #Format: image<n>.jpg, where n is indexed from zero
                cv2.imwrite(image_filename, image)

                #Other functions for image processing go here
                #generate 1-D histogram
                # hist = cv2.calcHist([image],[0],None,[256],[0,256])
                # plot histogram with intensity on x axis, 
                # number of pixels at each intensity along y
                # pyplot.plot(hist)
                # #save histogram as jpg
                # pyplot.savefig('histogram.jpg')
                
                #Vulnerable to corruption if handler is called here
                
                # output_filename = image_filename + '['+ str(count) + '].jpg'

                try:
                    file = open(output_filename, "a")
                except FileNotFoundError:
                    msg = "Terminal: " + output_filename + " does not exist"
                    print(msg)
                    sys.exit()
                #Primarily comma delimited
                file.write(pic_str)
                file.write(message.get_tag())
                #Secondary delimiter is newline
                file.write("\n")
                file.close()

                # time.sleep(2)#

    # else no motion is detected, keep sensing

motion_sensor.sensor_shutdown()