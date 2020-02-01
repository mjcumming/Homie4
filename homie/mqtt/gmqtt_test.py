import asyncio
import os
import signal
import time

from gmqtt import Client as MQTTClient


STOP = asyncio.Event()


def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('homie/#', qos=0)


def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:', topic, payload, qos, properties)


def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

def ask_exit(*args):
    STOP.set()

async def main(broker_host):
    client = MQTTClient("client-id")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    #client.set_auth_credentials(token, None)
    await client.connect(broker_host)

    client.publish('TEST/TIME', str(time.time()), qos=1)

    await STOP.wait()
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    host = 'openhab'
    #token = os.environ.get('FLESPI_TOKEN')

#    loop.add_signal_handler(signal.SIGINT, ask_exit)
#    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main(host))