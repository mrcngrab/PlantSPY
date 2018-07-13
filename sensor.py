import time
import RPi

class Sensor:

    __pin = 0
    __is_pull_up = None
    def __init__(self,pin,is_pull_up):
	self.__pin = pin
	self.__is_pull_up = is_pull_up 

    def read(self):
	self.__initializeSensor()        
	data = self.__getData()
	
    def write(self):
        pass;

    def __initializeSensor(self):
        #Init sensor by seting __pin as HIGH output for x ms
	#Set __pin as LOW output for 20 ms
	#Set __pin as INPUT with pullup software resistor if __is_pull_up = True
	#get data using __getData()
        pass;

    def __getData(self):
        pass;

    def setPin(self,pin,value):
        pass;
