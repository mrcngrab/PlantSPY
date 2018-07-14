import time
import datetime
import RPi.GPIO as GPIO

class Sensor:

    __pin = 0
    __start_time = 0
    __end_time = 0
    def __init__(self,pin):
	self.__pin = pin

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
	time.sleep(0.04)
	#Set __pin as LOW output for 20 ms
	GPIO.output(self.__pin,GPIO.LOW)
	time.sleep(0.02)
	#Set __pin as INPUT with pullup
        GPIO.setup(self.__pin,GPIO.IN,GPIO.PUD_UP)
	GPIO.add_event_detect(self.__pin,GPIO.RISING,__callback_on_high_input)
	GPIO.add_event_detect(self.__pin,GPIO.FALLING,__callback_on_low_input)
    def __getData(self):
	pass;

    def setPin(self,pin,value):
        pass;
    def __callback_on_high_input(self):
        self.__end_time = datetime.datetime.now()
	self.__diff_time = (self.__end_time - self.__start_time).total_seconds() * 1000
	print self.__diff_time
	pass;

    def __callback_on_low_input(self):
	#firts Falling edge
        if(self.__start_time == 0):
            self.__start_time = datetime.datetime.now()
	else:
	    self.__start_time = self.__end_time    
	pass;
