//******************************************************************
// Program #: funcs.h
//
// Programmer: Mehmet Kutlug/Dan Youngk
//
// Due Date: NA
//
// EGRE 347, Spring 2022       Instructor: Robert Klenke
//
// Pledge: I have neither given nor received unauthorized aid on this program.
//
// Description: Defines constant and declares functions used in funcs.cpp
//
// Input: none
//
// Output: none
//
//******************************************************************

//pin numbers used
const int IR_PIN = 4;
const int red = 24;
const int yellow = 5;
const int green = 16;
//delay between each photo taken in seconds
const int CAMERA_DELAY = 1;

//initialzes all leds and input pin for IR sensor
void pinInit();
//returns true if motion sensor detecs motion
bool senseMotion();
//turns off all led pins
void clearLED();