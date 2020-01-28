#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_state import Node_State

import logging

logger = logging.getLogger(__name__)


class Device_State(Device_Base):
    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
        state_values=None,
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        self.add_node(
            Node_State(
                self,
                id="state",
                name="State",
                state_values=state_values,
                set_state=self.set_state,
            )
        )

        self.start()

    def update_state(self, state):
        self.get_node("state").update_state(state)
        logger.debug("State Update {}".format(state))

    def set_state(self, state):  # received commands from clients
        # subclass must override and provide logic to set the device
        logger.debug("State Set {}".format(state))

