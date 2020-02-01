#!/usr/bin/env python

# not fully working

import asyncio
import os
import signal
import time
import threading
import functools


from gmqtt import Client as MQTTClient
from gmqtt.mqtt.constants import MQTTv311

from homie.mqtt.mqtt_base import MQTT_Base

import logging

logger = logging.getLogger(__name__)



class GMQTT_Client(MQTT_Base):
    def __init__(self, mqtt_settings):
        MQTT_Base.__init__(self, mqtt_settings)

        self.mqtt_client = None

    def connect(self):
        MQTT_Base.connect(self)

        self.mqtt_client = MQTTClient(
            'gmqtt'#self.mqtt_settings["MQTT_CLIENT_ID"]
        )

        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.on_disconnect = self._on_disconnect


        if self.mqtt_settings["MQTT_USERNAME"]:
            self.mqtt_client.set_auth_credentials(
                self.mqtt_settings["MQTT_USERNAME"],
                self.mqtt_settings["MQTT_PASSWORD"],
            )


        def start():
            try:
                logger.warning ('Connecting to MQTT')
                asyncio.set_event_loop(self.event_loop)
#                self.event_loop.run_until_complete(
 #                   self.mqtt_client.connect(self.mqtt_settings["MQTT_BROKER"], self.mqtt_settings["MQTT_PORT"],keepalive=self.mqtt_settings["MQTT_KEEPALIVE"], version=MQTTv311)
  #              )
                logger.warning ('Looping forever')
                self.event_loop.run_forever()
                logger.warning ('Event loop stopped')
                #self.session.close()
            except Exception as e:
                logger.error ('Error in event loop {}'.format(e))

        self.event_loop = asyncio.new_event_loop()

        logger.warning("Starting MQTT thread")
        self._ws_thread = threading.Thread(target=start, args=())

        self._ws_thread.daemon = True
        self._ws_thread.start()

        future = asyncio.run_coroutine_threadsafe(
            self.mqtt_client.connect(self.mqtt_settings["MQTT_BROKER"], self.mqtt_settings["MQTT_PORT"],keepalive=self.mqtt_settings["MQTT_KEEPALIVE"], version=MQTTv311),
            self.event_loop
        )

    def publish(self, topic, payload, retain, qos):
        MQTT_Base.publish(self, topic, payload, retain, qos)

        if self.mqtt_connected is True:
            wrapped = functools.partial(
                self.mqtt_client.publish,topic, payload, retain=retain, qos=qos
            )
            self.event_loop.call_soon_threadsafe(wrapped)
        else:
            logger.warning(
                "Device MQTT publish NOT CONNECTED: {}, retain {}, qos {}, payload: {}".format(
                    topic, retain, qos, payload
                )
            )



#        future = asyncio.run_coroutine_threadsafe(
 #           self.mqtt_client.publish(topic, payload, retain=retain, qos=qos),
  #          self.event_loop
   #     )

    def subscribe(self, topic, qos):  # subclass to provide
        MQTT_Base.subscribe(self, topic, qos)
        self.mqtt_client.subscribe(topic, qos)

    def unsubscribe(self, topic):  # subclass to provide
        MQTT_Base.unsubscribe(self, topic)
        self.mqtt_client.unsubscribe(topic)

    def set_will(self, will, topic, retain, qos):
        MQTT_Base.set_will(self, will, topic, retain, qos)
        #self.mqtt_client.will_set(will, topic, retain, qos)

    def _on_connect(self, client, flags, rc, properties):
        logger.info("MQTT On Connect: {}".format(rc))
        self.mqtt_connected = rc == 0

    def _on_message(self, client, topic, payload, qos, properties):
        #topic = msg.topic
        #payload = msg.payload.decode("utf-8")
        MQTT_Base._on_message(self, topic, payload, False , qos)

    def _on_disconnect(self, client, packet, exc=None):
        self.mqtt_connected = False  # note, change this uses the property setter, do not really need to catch this in the base class
        logger.warning(
            "MQTT Disconnection  {} {} {}".format(
                client, packet, exc
            )
        )
        MQTT_Base._on_disconnect(self, 0)

