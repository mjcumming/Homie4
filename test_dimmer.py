#!/usr/bin/env python

import time

from homie.device_dimmer import Device_Dimmer

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



mqtt_settings = {
    "MQTT_BROKER": "OpenHAB",
    "MQTT_PORT": 1883,
}


class My_Dimmer(Device_Dimmer):
    def set_dimmer(self, percent):
        print(
            "Received MQTT message to set the dimmer to {}. Must replace this method".format(
                percent
            )
        )
        super().set_dimmer(percent)


try:

    dimmer = My_Dimmer(
        name="Test Dimmer", device_id="testdimmer", mqtt_settings=mqtt_settings
    )

    while True:
        dimmer.update_dimmer(0)
        time.sleep(15)
        dimmer.update_dimmer(50)
        time.sleep(15)
        dimmer.update_dimmer(100)
        time.sleep(15)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    dimmer.close()
