#!/usr/bin/env python

import time

from homie.device_integer import Device_Integer

mqtt_settings = {
    "MQTT_BROKER": "OpenHAB",
    "MQTT_PORT": 1883,
}


class My_Integer(Device_Integer):
    def set_integer(self, value):
        print(
            "Received MQTT message to set the integer to {}. Must replace this method".format(
                value
            )
        )
        My_Integer.set_integer(self, value)


try:

    integer = My_Integer(name="Test Integer", mqtt_settings=mqtt_settings)

    while True:
        integer.update_value(0)
        time.sleep(5)
        integer.update_value(10)
        time.sleep(5)
        integer.update_value(20)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
