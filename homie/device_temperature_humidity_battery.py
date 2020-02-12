#!/usr/bin/env python

from homie.device_temperature_humidity import Device_Temperature_Humidity
from homie.node.property.property_battery import Property_Battery

import logging

logger = logging.getLogger(__name__)


class Device_Temperature_Humidity_Battery(Device_Temperature_Humidity):
    def register_status_properties(self, node):
        super(Device_Temperature_Humidity_Battery, self).register_status_properties(
            node
        )

        self.battery = Property_Battery(node)
        node.add_property(self.battery)

    def update_battery(self, battery):
        logger.info("Updated Battery {}".format(battery))
        self.battery.value = battery

