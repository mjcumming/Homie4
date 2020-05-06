#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base
from homie.node.property.property_button import Property_Button

import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class Device_Button(Device_Base):
    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        node = Node_Base(self, "button", "Button", "button")
        self.add_node(node)

        self.button = Property_Button(
                node,
                id="button",
                name="Button",
            )
        node.add_property(self.button)

        self.start()

    def push_button(self):
        self.button.push()
