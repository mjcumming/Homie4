#!/usr/bin/env python

import time

from homie.device_button import Device_Button

mqtt_settings = {
    "MQTT_BROKER": "192.168.1.81",
    "MQTT_PORT": 1883,
}


try:

    button = Device_Button(device_id="button",name="Test Button", mqtt_settings=mqtt_settings)

    while True:
        time.sleep(5)
        button.push_button()
        print ('button push')

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")

