# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build

# Include any dependencies generated for this target.
include utils/CMakeFiles/raspicam_test.dir/depend.make

# Include the progress variables for this target.
include utils/CMakeFiles/raspicam_test.dir/progress.make

# Include the compile flags for this target's objects.
include utils/CMakeFiles/raspicam_test.dir/flags.make

utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o: utils/CMakeFiles/raspicam_test.dir/flags.make
utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o: ../utils/raspicam_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o"
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o -c /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/utils/raspicam_test.cpp

utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam_test.dir/raspicam_test.cpp.i"
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/utils/raspicam_test.cpp > CMakeFiles/raspicam_test.dir/raspicam_test.cpp.i

utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam_test.dir/raspicam_test.cpp.s"
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/utils/raspicam_test.cpp -o CMakeFiles/raspicam_test.dir/raspicam_test.cpp.s

# Object files for target raspicam_test
raspicam_test_OBJECTS = \
"CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o"

# External object files for target raspicam_test
raspicam_test_EXTERNAL_OBJECTS =

utils/raspicam_test: utils/CMakeFiles/raspicam_test.dir/raspicam_test.cpp.o
utils/raspicam_test: utils/CMakeFiles/raspicam_test.dir/build.make
utils/raspicam_test: src/libraspicam.so.0.1.2
utils/raspicam_test: /opt/vc/lib/libmmal_core.so
utils/raspicam_test: /opt/vc/lib/libmmal_util.so
utils/raspicam_test: /opt/vc/lib/libmmal.so
utils/raspicam_test: utils/CMakeFiles/raspicam_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable raspicam_test"
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/raspicam_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
utils/CMakeFiles/raspicam_test.dir/build: utils/raspicam_test

.PHONY : utils/CMakeFiles/raspicam_test.dir/build

utils/CMakeFiles/raspicam_test.dir/clean:
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils && $(CMAKE_COMMAND) -P CMakeFiles/raspicam_test.dir/cmake_clean.cmake
.PHONY : utils/CMakeFiles/raspicam_test.dir/clean

utils/CMakeFiles/raspicam_test.dir/depend:
	cd /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/utils /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils /home/pi/network_drive/final/EGRE347_Final_Project/libraries/raspicam-master/build/utils/CMakeFiles/raspicam_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : utils/CMakeFiles/raspicam_test.dir/depend

