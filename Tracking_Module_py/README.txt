EGRE347 Final Project
Daniel J. Youngk, Mehmet Kutlug

First you must connect the G-mouse, and find out which port that the G_Mouse is using. This can be accomplished by listing available serial devices.

Find USB ACM in list.

Usage:dmesg | grep tty

This ID is usually "/dev/ttyACM0"

This module receives input from a G-mouse GPS receiver, and GPIO pins for input/output.
GPIO Pinout can be customized by editing the beginning of "Sensor_class.py"
Only GPGGA messages are utilized, terminal output will show what is being saved, when.
Circuit arrangement is found in "EGRE347_FinalProject_DanMehmet.pdf" [Figure 2]

Usage:python3 Tracking_Module.py /dev/<G-Mouse Identifier>

Output files will be named 'buffer_image[n]" and each additional immage will be logged with coordinates in location_log.
Output will be a detailed 'buffer' csv having columns delimited by commas, and rows delimited by newline.