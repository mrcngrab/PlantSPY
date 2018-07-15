
from sensor import Sensor
from RPi import GPIO as GPIO


def main():

#GPIO Init
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
#GPIO test
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,0)
#Sensor setup
    s = Sensor(pin = 14)
    s.read()
if __name__ == "__main__":
    main()

