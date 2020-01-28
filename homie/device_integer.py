#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_integer import Node_Integer

import logging

logger = logging.getLogger(__name__)


class Device_Integer(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(
            Node_Integer(self, id="integer", name="Integer", set_value=self.set_value)
        )

        self.start()

    def update_value(self, value):
        self.get_node("integer").update_value(value)
        logger.debug("Integer Update {}".format(value))

    def set_value(self, value):  # received commands from clients
        # subclass must override and provide logic to set the device
        logger.debug("Integer Set {}".format(value))

