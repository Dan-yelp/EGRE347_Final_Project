//******************************************************************
// Program #: funcs.cpp
//
// Programmer: Mehmet Kutlug/Dan Youngk
//
// Due Date: NA
//
// EGRE 347, Spring 2022       Instructor: Robert Klenke
//
// Pledge: I have neither given nor received unauthorized aid on this program.
//
// Description: Defines functions used in serial_read_start.cpp to initialize all pins used
//
// Input: none
//
// Output: none
//
//******************************************************************

using namespace std;

#include <fstream>
#include <ostream>
#include <raspicam/raspicam.h>
#include <string>
#include <wiringPi.h>
#include "funcs.h"


// void pinInit()
// 
// Summary of the pinInit() function: 
// 
//    Initialzes LED pins to output and IR sensor pin to input
// 
// Parameters   : none
// 
// Return Value : void
// 
void pinInit(){
    wiringPiSetupGpio();
    pinMode(IR_PIN, INPUT);
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
}

// void senseMotion()
// 
// Summary of the senseMotion() function: 
// 
//    Returns true if IR sensor pin is high, false otherwise
// 
// Parameters   : none
// 
// Return Value : bool
// 
bool senseMotion(){
    clearLED();

    if(digitalRead(IR_PIN)){
        digitalWrite(red, HIGH);
        return true;
    }
    
    return false;
}

// void clearLED()
// 
// Summary of the clearLED() function: 
// 
//    turns of all LEDs
// 
// Parameters   : none
// 
// Return Value : void
// 
void clearLED(){
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
}