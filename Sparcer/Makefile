CXX = g++
sparce : serial_read_start.o NMEA_GPS_sparce.o
	$(CXX) serial_read_start.o NMEA_GPS_sparce.o -o sparce

serial_read_start.o : serial_read_start.cpp
	$(CXX) -c serial_read_start.cpp

NMEA_GPS_sparce.o : NMEA_GPS_sparce.cpp
	$(CXX) -c NMEA_GPS_sparce.cpp

clean:
	rm *.o sparce*