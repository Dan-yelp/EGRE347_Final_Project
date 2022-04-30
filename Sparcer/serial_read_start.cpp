//******************************************************************
// Program #: Reading from serial port
//
// Programmer: Matthew Gelber/Robert Klenke
//
// Due Date: NA
//
// EGRE 347, Fall 2020       Instructor: Robert Klenke
//
// Pledge: I have neither given nor received unauthorized aid on this program.
//
// Description: C++ example for reading information from serial port one byte at a time
//
// Input: command line argument of the desired serial port
//
// Output: none
//
//******************************************************************
using namespace std;

#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <wiringPi.h>
#include <csignal>
#include "NMEA_GPS_sparce.h"

// global flag used to exit from the main loop
bool RUNNING = true;

// Callback handler if CTRL-C signal is detected
void my_handler(int s) 
{
    cout << "Detected CTRL-C signal no. " << s << '\n';
    RUNNING = false;
}

int main(int argc, char *argv[])
{
    signal(SIGINT, my_handler);//To handle a Ctrl+c
	unsigned char read_buff;

    GPS * gps = new GPS();

	bool quit_flag = false;

	ifstream infile;
	infile.open(argv[1], fstream::in);
	GPS * new_message = new GPS; 

	cout << argv[1] << endl;
	int sp = open(argv[1], O_RDONLY | O_NOCTTY | O_NDELAY);	//opens the serial port inputted as argument as read only

	if(sp < 0){
		cout << "unable to open port " << argv[1] << endl;
		exit(-1);
	}
	else
		cout << "port successfully opened" << endl;
	while(RUNNING)
	{
			// printf("Read byte:%x\n", read_buff);
			if(read(sp, &read_buff, sizeof(read_buff)))
				new_message->GPS_message(read_buff);
	}

	delete new_message;

	close(sp);
}
