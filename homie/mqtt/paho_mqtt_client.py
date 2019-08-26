#!/usr/bin/env python

import paho.mqtt.client as mqtt_client

import traceback

from uuid import getnode as get_mac
from homie.mqtt.mqtt_base import MQTT_Base

import logging
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

mqtt_logger = logging.getLogger('MQTT')
mqtt_logger.setLevel('INFO')


COONNECTION_RESULT_CODES = {
    0: 'Connection successful',
    1: 'Connection refused - incorrect protocol version',
    2: 'Connection refused - invalid client identifier',
    3: 'Connection refused - server unavailable',
    4: 'Connection refused - bad username or password',
    5: 'Connection refused - not authorised',
}

class PAHO_MQTT_Client (MQTT_Base): 

    def __init__(self, mqtt_settings):
        MQTT_Base.__init__(self,mqtt_settings)

        self.mqtt_client= None

    def connect(self):
        MQTT_Base.connect(self)

        self.mqtt_client = mqtt_client.Client(client_id=self.mqtt_settings['MQTT_CLIENT_ID'])
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        #self.mqtt_client.on_publish = self._on_publish
        self.mqtt_client.on_disconnect = self._on_disconnect
        self.mqtt_client.enable_logger(mqtt_logger)
        self.mqtt_client.enable_logger()

        if self.mqtt_settings ['MQTT_USERNAME']:
            self.mqtt_client.username_pw_set(
                    self.mqtt_settings ['MQTT_USERNAME'],
                    password=self.mqtt_settings ['MQTT_PASSWORD']
            )

        try:
            self.mqtt_client.connect(
                self.mqtt_settings ['MQTT_BROKER'],
                port=self.mqtt_settings ['MQTT_PORT'],
                keepalive=self.mqtt_settings ['MQTT_KEEPALIVE'],
            )

            self.mqtt_client.loop_start()

        except Exception as e:
            logger.warning ('MQTT Unable to connect to Broker {}'.format(e))

    def publish(self, topic, payload, retain=True, qos=0):
        MQTT_Base.publish(self,topic,payload,retain,qos)
        self.mqtt_client.publish(topic, payload, retain=retain, qos=qos)
    
    def subscribe(self, topic, qos=0): #subclass to provide
        MQTT_Base.subscribe(self,topic,qos)
        self.mqtt_client.subscribe(topic,qos)

    def unsubscribe(self, topic): #subclass to provide
        MQTT_Base.unsubscribe(self,topic)
        self.mqtt_client.unsubscribe(topic)

    def set_will(self,will,topic,retain=True,qos=1):
        MQTT_Base.set_will(self,will,topic,retain,qos)
        self.mqtt_client.will_set(will,topic,retain,qos)

    def _on_connect(self,client, userdata, flags, rc):
        logger.debug("MQTT On Connect: {}".format(rc))       
        self.mqtt_connected = (rc == 0)

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode("utf-8")
        MQTT_Base._on_message(self,topic,payload)

    def _on_disconnect(self,client,userdata,rc):
        self.mqtt_connected = False # note, change this uses the property setter, do not really need to catch this in the base class

        if rc > 0: #unexpected disconnect
            rc_text = 'Unknown result code {}'.format(rc)
            if rc in COONNECTION_RESULT_CODES:
                rc_text = COONNECTION_RESULT_CODES [rc]

            logger.warn ('MQTT Unexpected disconnection  {} {} {}'.format(client,userdata,rc_text))
        
        MQTT_Base._on_disconnect(self,rc)
        
