#!/usr/bin/env python

import time

from homie.device_contact import Device_Contact

mqtt_settings = {
    "MQTT_BROKER": "OpenHab",
    "MQTT_PORT": 1883,
}


try:

    contact = Device_Contact(
        name="Test Contact", device_id="testcontact", mqtt_settings=mqtt_settings
    )

    while True:
        time.sleep(5)
        contact.update_contact("OPEN")
        time.sleep(5)
        contact.update_contact("CLOSED")

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    quit()
