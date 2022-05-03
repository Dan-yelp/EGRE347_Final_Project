CXX = g++
FLAGS = -lwiringPi
FLAGS += -I/usr/local/include -lraspicam

sparce : serial_read_start.o NMEA_GPS_sparce.o
	$(CXX) serial_read_start.o NMEA_GPS_sparce.o $(FLAGS) -o sparce

serial_read_start.o : serial_read_start.cpp
	$(CXX) -c $(FLAGS) serial_read_start.cpp

NMEA_GPS_sparce.o : NMEA_GPS_sparce.cpp
	$(CXX) -c $(FLAGS) NMEA_GPS_sparce.cpp

clean:
	rm *.o sparce* *.ppm *.csv