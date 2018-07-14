import time
import RPi.GPIO as GPIO

class Sensor:

    __pin = 0
    __is_sw_pull_up = None
    def __init__(self,pin,is_sw_pull_up):
	self.__pin = pin
	self.__is_sw_pull_up = is_sw_pull_up 

    def read(self):
        #Initialize sensor to start sending data	
	self.__initializeSensor()        
	#get data using __getData()

	data = self.__getData()
	
    def write(self):
        pass;

    def __initializeSensor(self):
        #Set __pin as HIGH output for x ms
	GPIO.setup(self.__pin,GPIO.OUT)
	GPIO.output(self.__pin,GPIO.HIGH)
	time.sleep(0.06)
	#Set __pin as LOW output for 20 ms
	GPIO.output(self.__pin,GPIO.LOW)
	time.sleep(0.02)
	#Set __pin as INPUT with pullup software resistor if __is_sw_pull_up = True
	if(self.__is_sw_pull_up == True)
	    GPIO.setup(self.__pin,GPIO.IN,GPIO.PUD_UP)
	else
	    GPIO.setup(self.__pin,GPIO.IN)
        pass;

    def __getData(self):
        pass;

    def setPin(self,pin,value):
        pass;
