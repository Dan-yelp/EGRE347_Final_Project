//pin number for IR sensor
const int IR_PIN = 4;
const int red = 24;
const int yellow = 5;
const int green = 16;
//delay between each photo taken in seconds
const int CAMERA_DELAY = 1;

void pinInit();
bool senseMotion();
void clearLED();