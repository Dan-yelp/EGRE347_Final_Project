This program was written by Daniel J. Youngk, and Mehmet Kutlug.

NMEA message data scarcing.

First you must connect the G-mouse, and find out which port that the G_Mouse is using. This can be accomplished by listing available serial devices.

Usage: dmesg | grep tty

This will output the tty devices detected by kernel, in the order that they were detected and with a time stamp.

Using the call for the G-mouse port that is typically named "ttyACM0".

Usage: ./sparce /dev/ttyACM0