#!/usr/bin/env python

from homie.mqtt.paho_mqtt_client import PAHO_MQTT_Client

import logging
logger = logging.getLogger(__name__)

MQTT_SETTINGS = {
    'MQTT_BROKER' : None,
    'MQTT_PORT' : 1883,
    'MQTT_USERNAME' : None,
    'MQTT_PASSWORD' : None,
    'MQTT_KEEPALIVE' : 60,
    'MQTT_CLIENT_ID' : None,
    'MQTT_SHARE_CLIENT' : None,
}

mqtt_client_count = 0
    
def _mqtt_validate_settings(settings):
    settings = settings.copy()
    
    for setting,value in MQTT_SETTINGS.items():
        if not setting in settings:
            settings [setting] = MQTT_SETTINGS [setting]
        logger.debug ('MQTT Settings {} {}'.format(setting,settings [setting]))

    assert settings ['MQTT_BROKER']
    assert settings ['MQTT_PORT']

    ''' cannot use if two homie clients running from same pc
    if settings ['MQTT_CLIENT_ID'] is None or settings ['MQTT_SHARE_CLIENT'] is False:
        settings ['MQTT_CLIENT_ID'] = 'homiev3{:04d}'.format(mqtt_client_count) 
    '''
    
    return settings

common_mqtt_client = None

def connect_mqtt_client (device,mqtt_settings):
    global mqtt_client_count
    
    mqtt_settings = _mqtt_validate_settings (mqtt_settings)

    mqtt_client = None

    if mqtt_settings ['MQTT_SHARE_CLIENT'] is not True:

        logger.debug ('Using new MQTT client, number of instances {}'.format(mqtt_client_count))
        
        mqtt_client = PAHO_MQTT_Client (mqtt_settings)
        mqtt_client.connect()
        mqtt_client_count = mqtt_client_count + 1   

    else:
        logger.debug ('Using common MQTT client')

        global common_mqtt_client
        if common_mqtt_client is None:
            common_mqtt_client = PAHO_MQTT_Client (mqtt_settings)
            common_mqtt_client.connect()
            mqtt_client_count = mqtt_client_count + 1   

        mqtt_client = common_mqtt_client


    mqtt_client.add_device(device)

    return mqtt_client
   