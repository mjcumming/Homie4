# Raspberry PI 

import Adafruit_DHT
import time

from homie.device_temperature import Device_Temperature

mqtt_settings = {
    'MQTT_BROKER' : 'OpenHAB',
    'MQTT_PORT' : 1883,
}

try:

    temperature_device = Device_Temperature(device_id="temperature-sensor-1",name = "Temperature_Sensor 1",mqtt_settings=mqtt_settings)
    sensor = Adafruit_DHT.AM2302
    pin = 4

    
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print(temperature)
        temperature_device.update_temperature(temperature)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")  