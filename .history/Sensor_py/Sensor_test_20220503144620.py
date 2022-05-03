import Sensor_class

motion_sensor = Sensor_class.Sensor()

motion_sensor.sensor_init()

while(1):
    motion_sensor.sense_motion()
motion_sensor.sensor_shutdown()