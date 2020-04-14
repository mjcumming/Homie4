#!/usr/bin/env python


"""

Base MQTT Client for a Homie device

To allow for easy use of different MQTT clients

"""
from homie.support.network_information import Network_Information

network_info = Network_Information()

import logging

logger = logging.getLogger(__name__)


MQTT_SETTINGS = {
    "MQTT_BROKER": None,
    "MQTT_PORT": 1883,
    "MQTT_USERNAME": None,
    "MQTT_PASSWORD": None,
    "MQTT_KEEPALIVE": 60,
    "MQTT_CLIENT_ID": None,
    "MQTT_SHARE_CLIENT": False,
}


class MQTT_Base(object):
    def __init__(self, mqtt_settings, last_will):
        logger.debug("MQTT client Settings {}".format(mqtt_settings))

        self.last_will = last_will

        self.using_shared_mqtt_client = mqtt_settings["MQTT_SHARE_CLIENT"]

        self.mqtt_settings = mqtt_settings

        self._mqtt_connected = False

        self.ip_address = None
        self.mac_address = None

        self.homie_devices = []

    @property
    def mqtt_connected(self):
        return self._mqtt_connected

    @mqtt_connected.setter
    def mqtt_connected(self, connected):
        if connected != self._mqtt_connected:
            logger.debug("MQTT Connected is {} ".format(connected))
            self._mqtt_connected = connected
            for device in self.homie_devices:
                if device.start_time is not None:
                    device.mqtt_on_connection(connected)

    def connect(
        self,
    ):  # called by the device when its ready for the mqtt client to start, subclass to provide
        logger.debug(
            "MQTT Connecting to {} as client {}".format(
                self.mqtt_settings["MQTT_BROKER"], self.mqtt_settings["MQTT_CLIENT_ID"]
            )
        )

    def publish(self, topic, payload, retain, qos):  # subclass to provide
        logger.debug(
            "MQTT publish topic: {}, payload: {}, retain {}, qos {}".format(
                topic, payload, retain, qos
            )
        )

    def subscribe(self, topic, qos):  # subclass to provide
        logger.debug("MQTT subscribe  topic: {}, qos {}".format(topic, qos))

    def unsubscribe(self, topic):  # subclass to provide
        logger.debug("MQTT unsubscribe  topic: {}".format(topic))

    def set_will(self, will, topic, retain, qos):  # subclass to provide
        logger.info("MQTT set will {}, topic {}".format(will, topic))

    def get_mac_ip_address(self):
        if self.ip_address is None:
            self.ip_address = network_info.get_local_ip(
                self.mqtt_settings["MQTT_BROKER"], self.mqtt_settings["MQTT_PORT"]
            )

        if self.mac_address is None:
            self.mac_address = network_info.get_local_mac_for_ip(self.ip_address)

        return self.mac_address, self.ip_address

    def _on_message(self, topic, payload, retain, qos):
        logger.debug(
            "MQTT On Message: Topic {}, Payload {} Reatin {} QOS {}".format(
                topic, payload, retain, qos
            )
        )
        for device in self.homie_devices:
            if device.start_time is not None:  # device is ready
                try:
                    device.mqtt_on_message(topic, payload, retain == 1, qos)
                except:
                    logger.exception("on_message error")

    def _on_disconnect(self, rc):
        logger.warning("MQTT On Disconnect: Result Code {}".format(rc))
        self.mqtt_connected(False)

    def add_device(self, device):
        self.homie_devices.append(device)

    def remove_device(self, device):  # not tested
        del self.homie_devices[device]

    def close(self):
        logger.info("MQTT Closing")
