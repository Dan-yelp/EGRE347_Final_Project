#******************************************************************
# Program #: Reading from serial port
#
# Programmer: Robert Klenke
#
# Due Date: NA
#
# EGRE 347, Spring 2022       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python example for reading information from serial port one byte at a time
#
# Input: command line argument of the desired serial port
#
# Output: none
#
#******************************************************************

import sys
import GPS_class
#import RPi.GPIO as GPIO #Adds support of using GPIO pins

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
    message.read_byte(byte)
