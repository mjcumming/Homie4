#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_dimmer import Node_Dimmer
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Device_Dimmer(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Dimmer(self, id="dimmer", set_dimmer=self.set_dimmer))

        self.start()

    def update_dimmer(self, percent):  # sends updates to clients
        self.get_node("dimmer").update_dimmer(round(percent, 0))
        logger.debug("Dimmer Update {}".format(percent))

    def set_dimmer(self, percent):  # received commands from clients
        logger.debug("Dimmer Set {}".format(round(percent, 0)))

#    def publish_homeassistant(self):
#        hass_config = f'homeassistant/light/{self.device_id}/config'
#        hass_payload = f'{{"name": "{self.name}","command_topic": "homie/{self.device_id}/dimmer/dimmer/set","brightness_command_topic": "homie/{self.device_id}/dimmer/dimmer/set","brightness_state_topic": "homie/{self.device_id}/dimmer/dimmer","state_topic": "homie/{self.device_id}/dimmer/power","on_command_type": "brightness","brightness_scale": "100"}}'
#        super().publish_homeassistant(hass_config,hass_payload)

