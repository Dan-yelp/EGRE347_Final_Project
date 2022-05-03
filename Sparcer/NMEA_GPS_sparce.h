//******************************************************************
// Program #: HEADER for Sparcing data of NMEA protocol.
//
// Programmer: Daniel J. Youngk
//
// Due Date: NA
//
// EGRE 347, Fall 2020       Instructor: Robert Klenke
//
// Pledge: I have neither given nor received unauthorized aid on this program.
//
// Description: Header file for the GPS class. The implimentation file contains descriptions of each function
//              The data members of this class are used to temporarily store values pertaining to a message
//              while it is being sparced. The Private members are used implicitly as 'this', and memory mana-
//              -gement is performed within the driver.
//
// Input:single char containing one byte of data from NMEA serial protocal.
//
// Output: string that is called tye
//-----------------------------------------------------------------------

//	Data members:
//Strings - state name, type of message, and data from the buffer
//Package - enumerated type for GPS format message description
//unsigned char - one byte of buffer data in ascii format, check sumtracker
using namespace std;
enum GPS_state{Reading,Found_Init, Found_Type, Found_Data, Writing};

const int GPGGA_LENGTH = 69;

class GPS
{
	private:
		enum GPS_state State;		// Holds current state the traffic light is in
		string to_GPS_message;				// string to GPS_message
		string Data_string;
		string Type_string;
		string Check_string;
		string Type_selection;
		float init_longitude;
		float init_latitude;
		float current_long;
		float current_lat;
        int Check_int;
		time_t *start;
		time_t *finish;
		
	public:
		GPS();				// Constructor
		
		~GPS();					// Destructor
	
	
		bool GPS_message(char c);			// Main implementation for the state machine
};
