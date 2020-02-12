#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base

from homie.node.property.property_setpoint import Property_Setpoint
from homie.node.property.property_temperature import Property_Temperature
from homie.node.property.property_humidity import Property_Humidity
from homie.node.property.property_enum import Property_Enum
from homie.node.property.property_string import Property_String

import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# example
THERMOSTAT_SETTINGS = {
    "current_temperature": 70,
    "current_humidity": 30,
    "cool_setpoint": 70,
    "max_cool_setpoint": 90,
    "min_cool_setpoint": 60,
    "heat_setpoint": 70,
    "max_heat_setpoint": 90,
    "min_heat_setpoint": 60,
    "fan_mode": "On",
    "fan_modes": ["On", "Auto"],
    "hold_mode": "Schedule",
    "hold_modes": ["Schedule", "Temporary", "Permanent"],
    "system_mode": "Off",
    "system_modes": ["Off", "Heat", "Cool", "Auto"],
    "system_status": "Idle",
    "units": "F",
}


class Device_Thermostat(Device_Base):
    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
        thermostat_settings=THERMOSTAT_SETTINGS,
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        node = Node_Base(self, "controls", "Controls", "controls")
        self.add_node(node)

        if "heat_setpoint" in thermostat_settings:
            heat_setpt_limits = "{}:{}".format(
                thermostat_settings["min_heat_setpoint"],
                thermostat_settings["max_heat_setpoint"],
            )
            self.heat_setpoint = Property_Setpoint(
                node,
                id="heatsetpoint",
                name="Heat Setpoint",
                data_format=heat_setpt_limits,
                unit=thermostat_settings["units"],
                value=thermostat_settings["heat_setpoint"],
                set_value=self.set_heat_setpoint,
            )
            node.add_property(self.heat_setpoint)

        if "cool_setpoint" in thermostat_settings:
            cool_setpt_limits = "{}:{}".format(
                thermostat_settings["min_cool_setpoint"],
                thermostat_settings["max_cool_setpoint"],
            )
            self.cool_setpoint = Property_Setpoint(
                node,
                id="coolsetpoint",
                name="Cool Setpoint",
                data_format=cool_setpt_limits,
                unit=thermostat_settings["units"],
                value=thermostat_settings["cool_setpoint"],
                set_value=self.set_cool_setpoint,
            )
            node.add_property(self.cool_setpoint)

        if "system_mode" in thermostat_settings:
            self.system_mode = Property_Enum(
                node,
                id="systemmode",
                name="System Mode",
                data_format=",".join(thermostat_settings["system_modes"]),
                value=thermostat_settings["system_mode"],
                set_value=self.set_system_mode,
            )
            node.add_property(self.system_mode)

        if "fan_mode" in thermostat_settings:
            self.fan_mode = Property_Enum(
                node,
                id="fanmode",
                name="Fan Mode",
                data_format=",".join(thermostat_settings["fan_modes"]),
                value=thermostat_settings["fan_mode"],
                set_value=self.set_fan_mode,
            )
            node.add_property(self.fan_mode)

        if "hold_mode" in thermostat_settings:
            self.hold_mode = Property_Enum(
                node,
                id="holdmode",
                name="Hold Mode",
                data_format=",".join(thermostat_settings["hold_modes"]),
                value=thermostat_settings["hold_mode"],
                set_value=self.set_hold_mode,
            )
            node.add_property(self.hold_mode)

        node = Node_Base(self, "status", "Status", "status")
        self.add_node(node)

        self.current_temperture = Property_Temperature(
            node,
            unit=thermostat_settings["units"],
            value=thermostat_settings["current_temperature"],
        )
        node.add_property(self.current_temperture)

        self.current_humidity = Property_Humidity(
            node, value=thermostat_settings["current_humidity"]
        )
        node.add_property(self.current_humidity)

        self.system_status = Property_String(
            node,
            id="systemstatus",
            name="System Status",
            value=thermostat_settings["system_status"],
        )
        node.add_property(self.system_status)

        self.start()

    def update_heat_setpoint(self, value):
        self.heat_setpoint.value = value

    def update_cool_setpoint(self, value):
        self.cool_setpoint.value = value

    def update_system_mode(self, value):
        self.system_mode.value = value

    def update_system_status(self, value):
        self.system_status.value = value

    def update_fan_mode(self, value):
        self.fan_mode.value = value

    def update_hold_mode(self, value):
        self.hold_mode.value = value

    def update_current_temperature(self, value):
        self.current_temperture.value = value

    def update_current_humidity(self, value):
        self.current_humidity.value = value

    def set_heat_setpoint(self, value):
        logger.debug("Heat Set {}".format(value))

    def set_cool_setpoint(self, value):
        logger.debug("Cool Set {}".format(value))

    def set_system_mode(self, value):
        logger.debug("Mode Set {}".format(value))

    def set_fan_mode(self, value):
        logger.debug("Fan Set {}".format(value))

    def set_hold_mode(self, value):
        logger.debug("Hold Set {}".format(value))
