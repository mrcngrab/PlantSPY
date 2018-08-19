
import RPi.GPIO as GPIO
import dht11
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor1 = 14
instance1 = dht11.DHT11(pin=sensor1)

dht11Sensors = {
        1 : {'name': 'sensor1', 'instance': instance1, 'name_t' : 'Temperature', 'value_t' : "0C",
        'name_h' : 'Humidity', 'value_h' : "0%"}
        }
for sensor in dht11Sensors:
    result = dht11Sensors[sensor]['instance'].read()
    if result.is_valid():
        dht11Sensors[sensor]['value_t'] = result.temperature
        dht11Sensors[sensor]['value_h'] = result.humidity
        print("Temperature: %d C" % dht11Sensors[sensor]['value_t'])
        print("Humidity: %d %%" % dht11Sensors[sensor]['value_h'])
    else:
        dht11Sensors[sensor]['value_t'] = "Error :%d " % result.error_code
        dht11Sensors[sensor]['value_h'] = "Error :%d " % result.error_code
        print(dht11Sensors[sensor]['value_t'])


@app.route("/")
def main():
    tempData = {
        'dht11Sensors' : dht11Sensors
        }
    return render_template('main.html', **tempData)

if __name__ == "__main__":
#When running with debug=True, Sensor will show error becouse of reload
    app.run(host='0.0.0.0', port=80, debug=False)
