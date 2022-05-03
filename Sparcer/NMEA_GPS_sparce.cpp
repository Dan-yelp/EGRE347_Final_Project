//-----------------------------------------------------------------------
// File : NMEA_GPS_sparce.cpp
//
// Programmer: Daniel J. Youngk
//
// Creation Date:4/11/22
//
// Description: Class implimentation file for GPS messages. Developed for receiving and echoing
// serial sattelite data of the types GPGGA, GPGSA, GPGSV, or GPRMC. A stand alone state machine
// that operates off a buffer, one character at a time. The states are defined as enumerated types.

#include <iostream>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <time.h>
#include "NMEA_GPS_sparce.h"

using namespace std;

GPS::GPS()
{
	Data_string = "";											
	State = Reading;											
}

GPS::~GPS()			// destructor
{}

bool GPS::GPS_message(char c)
{
	if(c == '$') 
	{
		State = Found_Init;
		Data_string.clear();
		Check_string.clear();
		Type_string.clear();
		time(start);

		Check_int = 0;
	}

	else if(State == Found_Init) 
	{
		Type_string += c;
		Data_string += c;

		if(Type_string == "GPGGA")// || Type_string == "GPGSA" || Type_string == "GPGSV" || Type_string == "GPRMC")
			State = Found_Type;

		Check_int ^= c;
    }

	else if(State == Found_Type) 
	{
		if(c == '*')
			State = Found_Data;

		else 
		{
			Check_int ^= c;
			Data_string += c;
		}
	}

	else if(State == Found_Data)
	{

		if(c != '*')
			Check_string += c;

		if (Check_string.length() == 2)
		{
			stringstream cs;
			int x;
			cs << hex << Check_string;
			cs >> x;
			State = (x == Check_int) ? Writing : Reading;
		}	
	}

	else if(State == Writing)
	{
		time(finish);
		// stringstream ss;
		// float y;
		// ss << float << Data_string.substr(16,26)//from string to float?
		// ss >> y;
		// cout<<endl<<"y:"<<y<<endl;
		if(Data_string.length() == GPGGA_LENGTH){
			cout<<endl<<"Longitude: "<<Data_string.substr(16,2)<<" degrees, "<<Data_string.substr(18,8)<<" minutes"<<endl;	
			cout<<"Latitude: "<<Data_string.substr(29,3)<<" degrees, "<<Data_string.substr(32,8)<<" minutes"<<endl;
			cout<<"Time: "<<Data_string.substr(6,9)<<endl;
			cout<<"Execution Time: "<<*finish - *start<<endl;
		}
		// cout<<"Longitude:"<<Data_string.substr(6,9)<<endl;
		// cout<<"Message type:"<<Type_string<<endl;
		// cout<<"Message data:"<<Data_string<<endl;
		// cout<<"Message checksum:"<<Check_string<<endl;
		return true;
	}
	
	return false;		
}