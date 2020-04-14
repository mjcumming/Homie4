#!/usr/bin/env python

from homie.mqtt.paho_mqtt_client import PAHO_MQTT_Client
#from homie.mqtt.gmqtt_client import GMQTT_Client

MQTT_Client = PAHO_MQTT_Client

import logging

logger = logging.getLogger(__name__)

MQTT_SETTINGS = {
    "MQTT_BROKER": None,
    "MQTT_PORT": 1883,
    "MQTT_USERNAME": None,
    "MQTT_PASSWORD": None,
    "MQTT_KEEPALIVE": 60,
    "MQTT_CLIENT_ID": None,
    "MQTT_SHARE_CLIENT": None,
}

mqtt_client_count = 0
mqtt_clients = []


def _mqtt_validate_settings(settings):
    settings = settings.copy()

    for setting, value in MQTT_SETTINGS.items():
        if not setting in settings:
            settings[setting] = MQTT_SETTINGS[setting]
        logger.debug("MQTT Settings {} {}".format(setting, settings[setting]))

    assert settings["MQTT_BROKER"]
    assert settings["MQTT_PORT"]

    """ cannot use if two homie clients running from same pc
    if settings ['MQTT_CLIENT_ID'] is None or settings ['MQTT_SHARE_CLIENT'] is False:
        settings ['MQTT_CLIENT_ID'] = 'homiev3{:04d}'.format(mqtt_client_count) 
    """

    return settings


common_mqtt_client = None


def connect_mqtt_client(device, mqtt_settings):
    global mqtt_client_count

    mqtt_settings = _mqtt_validate_settings(mqtt_settings)

    mqtt_client = None

    last_will_topic = "/".join((device.topic, "$state"))

    if mqtt_settings["MQTT_SHARE_CLIENT"] is not True:

        logger.info(
            "Using new MQTT client, number of instances {}".format(mqtt_client_count)
        )

        mqtt_client = MQTT_Client(mqtt_settings, last_will_topic)
        mqtt_client.connect()
        mqtt_client_count = mqtt_client_count + 1
        mqtt_clients.append(mqtt_client)

    else:
        logger.info("Using common MQTT client")

        global common_mqtt_client
        if common_mqtt_client is None:
            common_mqtt_client = MQTT_Client(mqtt_settings,last_will_topic)
            common_mqtt_client.connect()
            mqtt_client_count = mqtt_client_count + 1
            mqtt_clients.append(mqtt_client)

        mqtt_client = common_mqtt_client

    mqtt_client.add_device(device)

    return mqtt_client

def close_mqtt_clients():
    logger.info ('Closing MQTT clients')
    for client in mqtt_clients:
        client.close()