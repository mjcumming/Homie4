#!/usr/bin/env python

import logging

from homie.device_status import Device_Status
from homie.node.property.property_temperature import Property_Temperature

logger = logging.getLogger(__name__)


class Device_Temperature(Device_Status):
    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
        temp_units="F",
    ):
        self.temp_units = temp_units

        super().__init__(device_id, name, homie_settings, mqtt_settings)

    def register_status_properties(self, node):
        self.temperature = Property_Temperature(node, unit=self.temp_units)
        node.add_property(self.temperature)

    def update_temperature(self, temperature):
        logger.info("Updated Temperature {}".format(temperature))
        self.temperature.value = temperature

