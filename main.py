
from sensor import Sensor
from RPi import GPIO as GPIO


def main():
    s = Sensor()
    s.initializeSensor()
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,0)


if __name__ == "__main__":
    main()

