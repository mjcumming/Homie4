#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_contact import Node_Contact
from homie.node.property.property_contact import Property_Contact
import logging

import time

logger = logging.getLogger(__name__)

mqtt_settings = {
    "MQTT_BROKER": "openhab",
    "MQTT_PORT": 1883,
}


class Device_Contact(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Contact(self, id="contact"))

        self.start()

    def update_contact(self, state):
        self.get_node("contact").update_contact(state)
        logging.info("Contact Update {}".format(state))


try:

    contact = Device_Contact(name="Test Contact", mqtt_settings=mqtt_settings)

    while True:
        time.sleep(5)

        node = contact.get_node("contact")
        node.add_property(Property_Contact(node, id="contactdynamic"))

        contact.update_contact("OPEN")

        time.sleep(5)

        node = contact.get_node("contact")
        node.remove_property("contactdynamic")

        contact.update_contact("CLOSED")

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    contact = None

