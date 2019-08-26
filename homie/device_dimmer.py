#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_dimmer import Node_Dimmer
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


class Device_Dimmer(Device_Base):

    def __init__(self, device_id=None, name=None, homie_settings=None, mqtt_settings=None):
        super().__init__ (device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Dimmer(self,id='dimmer',set_dimmer=self.set_dimmer))

        self.start()

    def update_dimmer(self,percent): #sends updates to clients
        self.get_node('dimmer').update_dimmer(percent)
        logger.debug ('Dimmer Update {}'.format(percent))

    def set_dimmer(self,percent):#received commands from clients
        logger.debug ('Dimmer Set {}'.format(percent))
