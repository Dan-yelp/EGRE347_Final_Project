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
#include <raspicam/raspicam.h>
#include <time.h>
#include "NMEA_GPS_sparce.h"

//pin number for IR sensor
const int IR_PIN = 17;
//delay between each photo taken in seconds
const int CAMERA_DELAY = 1;
//name of txt file that .ppm filenames and coordinates are saved to
//NOTE: program appends to file doesn't replace it
const string CSVFILE = "coordinates.csv";

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
	// Initialize wiringPi and allow the use of BCM pin numbering
	wiringPiSetupGpio();
    signal(SIGINT, my_handler);//To handle a Ctrl+c

	ofstream GPS_output;
	struct tm *t;
	time_t buff;
	string outfileName, last_coord;
	unsigned char read_buff;

	GPS_output.open(CSVFILE, std::ios_base::app);
	if(!GPS_output.is_open()){
		perror("Couldn't open outfile\n");
		exit(-1);
	}

	//following code copied for settin up picamera: https://github.com/cedricve/raspicam
	raspicam::RaspiCam Camera; //Camera object
	//Open camera 
	cout<<"Opening Camera..."<<endl;
	if ( !Camera.open()) {cerr<<"Error opening camera"<<endl;return -1;}
	//wait a while until camera stabilizes
	cout<<"Sleeping for 3 secs"<<endl;
	sleep(3);

    GPS * gps = new GPS();

	pinMode(IR_PIN, INPUT);

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
		if(read(sp, &read_buff, sizeof(read_buff)))
			if(new_message->GPS_message(read_buff))
				last_coord = new_message->get_Coord();
		
		//Enters if statement if IR sensor is outputting high
		if(digitalRead(17)){
			time(&buff);
			t = localtime(&buff);		
			outfileName = string("capture_") + to_string(t->tm_mon) + to_string(t->tm_mday) + to_string(t->tm_hour) + to_string(t->tm_min) + to_string(t->tm_sec) + ".ppm";		
			//capture
			Camera.grab();
			//allocate memory
			unsigned char *data=new unsigned char[  Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB )];
			//extract the image in rgb format
			Camera.retrieve ( data);//get camera image
			//save
			ofstream outFile ( outfileName,std::ios::binary );
			outFile<<"P6\n"<<Camera.getWidth() <<" "<<Camera.getHeight() <<" 255\n";
			outFile.write ( ( char* ) data, Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB ) );
			cout<<"Image saved at "<<outfileName<<endl;

			GPS_output << "File name," << outfileName << ",Coords," << last_coord << endl;
		}

			sleep(CAMERA_DELAY);
	}

	delete new_message;

	close(sp);
}
