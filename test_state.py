#!/usr/bin/env python

import time

from homie.device_state import Device_State

mqtt_settings = {
    "MQTT_BROKER": "QueenMQTT",
    "MQTT_PORT": 1883,
}


# states allowed for this device
STATES = "A,B,C,D,E"


class My_State(Device_State):
    def set_state(self, state):
        print(
            "Received MQTT message to set the state to {}. Must replace this method".format(
                state
            )
        )
        super().set_state(state)


try:

    state = My_State(
        name="Test State", mqtt_settings=mqtt_settings, state_values=STATES
    )

    while True:
        time.sleep(5)
        state.update_state("A")
        time.sleep(5)
        state.update_state("B")
        time.sleep(5)
        state.update_state("G")

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
