#!/usr/bin/env python

import time

from homie.device_boolean import Device_Boolean

mqtt_settings = {
    "MQTT_BROKER": "OPENHAB",
    "MQTT_PORT": 1883,
}


class My_Boolean(Device_Boolean):
    def set_switch(self, onoff):
        print(
            "Received MQTT message to set the switch to {}. Must replace this method".format(
                onoff
            )
        )
        super().set_switch(onoff)


try:

    switch = My_Boolean(name="Test Switch", mqtt_settings=mqtt_settings)

    while True:
        time.sleep(5)
        switch.update_boolean(True)
        time.sleep(5)
        switch.update_boolean(False)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    switch = None

