#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_boolean import Node_Boolean
import logging

logger = logging.getLogger(__name__)


class Device_Boolean(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Boolean(self, id="boolean", set_boolean=self.set_boolean))

        self.start()

    def update_boolean(self, boolean):  # sends updates to clients
        self.get_node("boolean").update_boolean(boolean)
        logger.debug("Boolean Update {}".format(boolean))

    def set_boolean(self, boolean):  # received commands from clients
        logger.debug("Boolean Set {}".format(boolean))

