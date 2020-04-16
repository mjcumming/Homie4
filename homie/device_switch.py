#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_switch import Node_Switch
import logging

logger = logging.getLogger(__name__)


class Device_Switch(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Switch(self, id="switch", set_switch=self.set_switch))

        self.start()

    def update_switch(self, onoff):  # sends updates to clients
        self.get_node("switch").update_switch(onoff)
        logger.debug("Switch Update {}".format(onoff))

    def set_switch(self, onoff):  # received commands from clients
        logger.debug("Switch Set {}".format(onoff))


    #def publish_homeassistant(self):
    #    hass_config = f'homeassistant/switch/{self.device_id}/config'
    #    hass_payload =  f'{{"name": "{self.name}","command_topic": "homie/{self.device_id}/switch/switch/set","state_topic": "homie/{self.device_id}/switch/switch","state_on" : "true","state_off" : "false","payload_on" : "true","payload_off" : "false"}}'

    #    super().publish_homeassistant(hass_config,hass_payload)

