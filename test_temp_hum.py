#!/usr/bin/env python

import time

from homie.device_temperature_humidity import Device_Temperature_Humidity

mqtt_settings = {
    "MQTT_BROKER": "QueenMQTT",
    "MQTT_PORT": 1883,
}


try:

    temp_hum = Device_Temperature_Humidity(name="Temp Hum", mqtt_settings=mqtt_settings)

    while True:
        temp_hum.update_temperature(50)
        temp_hum.update_humidity(10)
        time.sleep(5)
        temp_hum.update_temperature(10)
        temp_hum.update_humidity(30)
        time.sleep(5)
        temp_hum.update_temperature(90)
        temp_hum.update_humidity(90)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
