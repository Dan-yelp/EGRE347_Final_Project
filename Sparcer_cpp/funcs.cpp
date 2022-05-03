using namespace std;

#include <fstream>
#include <ostream>
#include <raspicam/raspicam.h>
#include <string>
#include <wiringPi.h>
#include "funcs.h"

void pinInit(){
    wiringPiSetupGpio();
    pinMode(IR_PIN, INPUT);
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
}

bool senseMotion(){
    clearLED();

    if(digitalRead(IR_PIN)){
        digitalWrite(red, HIGH);
        return true;
    }
    
    return false;
}

void clearLED(){
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
}