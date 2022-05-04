#******************************************************************
# Program #: Homework 8, GPS class to sparce NMEA messages. 
#
# Programmer: Daniel J. Youngk
#
# Due Date: NA
#
# EGRE 347, Spring 2022       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: GPS class for sparcing and descriminating type of NMEA protocol
#              messages. One byte is sent to the member function read_byte()
#              The class member on which read_byte is called updates to maint-
#              -ain effective state of the FSM. Any messages that do not meet 
#              the protocol standard are discarded. If a message is complete,
#              and the check cum matches, it is printed to terminal.
#              The data members 
#              store pertinant information for each message. Messages
#              can be seperated into different types by referring to the
#              Type_string. This class implaments a state machine that
#              operates on one byte of data at a time. 
#              
#
# Input: one byte from message buffer
#
# Output: Message type, data, and checksum
#
# References: https://www.easytweaks.com/python-string-hex-conversion/ - string to hex syntax
#             https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods - ord() syntax
#             https://docs.python.org/3/library/functions.html - string to hex, and ord syntax (very useful!!!)
#             http://aprs.gids.nl/nmea/ - NMEA protocol standard
#******************************************************************
class GPS:

    GPGGA_LENGTH = 69 #update this value

    #Data members for state machine
    State = "Reading"#Initial state, looking for $
    Data_string = str()#Used to store previous data for current message
    Check_string = str()#A string rep. of the check sum as read after *
    Type_string = str()#Type of message format, can be GPGGA, GPGSA, GPGSV, or GPRMC
    Check_int = int()#An integer rep. of the current check sum calculated
    tag_data = str()#Last known location

    #Default constructor
    def GPS():
        State = "Reading"

    def get_tag(self):
        return(self.tag_data)


    # Summary of the function: This is the main implimentation of the sparcing modulself. One byte
    # from the input buffer is used to determine the next transition of the FSM. Once initiated
    # with the character "$", this function reads in type, data, or check sum based on it's state.
    # Once a full message and check sum have been compared, the message and data are printed to 
    # terminal. 
    #
    # Parameters   : GPS class object (c), and Bytes containing one byte of ascii data
    # Return Value : NONE

    # Description: Loops and iterates from beginning to end of Part list using a vector container iterator.
    #             Reads in user input from std::cin and stores it as a string, compares it with "q" and if
    #             it is "q" then the printing is aborted, any other entry will contue the printing.
    def read_byte(self,e):
        #Convert from byte to string
        e = e.decode("ascii")
        #State 0 - Initializes a new message (state transition), data is reset if not empty
        if(e == '$'):
            self.State = "Found_Init"
            #Reset data members for new message
            self.Data_string = str()
            self.Check_string = str()
            self.Type_string = str()
            self.Check_int = 0
        #State 1 - Receives message type into a string, and only accepts one of the formentioned types
        elif(self.State == "Found_Init"): 
            self.Type_string += e
            self.Data_string += e
            #Once a complete type has been read, transition to next state
            if(self.Type_string == "GPGGA"):# or self.Type_string == "GPGSA" or self.Type_string == "GPGSV" or self.Type_string == "GPRMC"):
                self.State = "Found_Type"
            #Converts x from string to ascii decimal
            y = ord(e)
            #calculate check sum
            self.Check_int ^= y
        #State 2 - Receives data contained in message
        elif(self.State == "Found_Type"):
            #Indication of end of message, transition to next state if data is * 
            if(e == '*'):
                self.State = "Found_Data"
            #Calculate check sum and move to next data
            else:
                #Convert from string to integer
                y = ord(e)
                self.Check_int ^= y
                self.Data_string += e
        #State 3 - Calculates and compares check sum to determine message validity
        elif(self.State == "Found_Data"):
            #Temp string for storing previous value of check sum input without adding it to the data
            self.Check_string += e
            if (len(self.Check_string) == 2):
                #Convert string to integer of it's ascii hex value
                x = self.Check_string
                y = int(x,16)
                #If the check sum matches, proceed to process or display GPS data
                if(y == self.Check_int):
                    self.State = "Writing"
                else:
                    self.State = "Reading"
        #State 4 - Output message to terminal, or wrap up data tag
        if self.State == "Writing" and self.Type_string == 'GPGGA' and (len(self.Data_string) is 69): #and len(self.Data_string) == GPGGA_LENGTH:
            # print('Message type:',self.Type_string)
            print('GPGGA message data:',self.Data_string)
            # print('Message checksum:',self.Check_string,'\n')
            self.tag_data = self.Data_string[6:16] + self.Data_string[16:25] + self.Data_string[28:41]
            print('Tag data:', self.tag_data)
            print('String length:',len(self.Data_string))
            return True
        elif self.State is "Writing":
            print('String length:',len(self.Data_string))
            # print('Message type:',self.Type_string)
            # print('Message data:',self.Data_string)
            # print('Message checksum:',self.Check_string,'\n')
            
        return False


