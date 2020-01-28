#!/usr/bin/env python

from homie.device_temperature import Device_Temperature
from homie.node.property.property_humidity import Property_Humidity

import logging

logger = logging.getLogger(__name__)


class Device_Temperature_Humidity(Device_Temperature):
    def register_status_properties(self, node):
        super(Device_Temperature_Humidity, self).register_status_properties(node)

        self.humidity = Property_Humidity(node)
        node.add_property(self.humidity)

    def update_humidity(self, humidity):
        logger.info("Updated Humidity {}".format(humidity))
        self.humidity.value = humidity

