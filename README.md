# Homie

Python implementation of Homie 3.0.1

Class based system to easily add Homie 3.0.1 support to devices.

Install

~~~~
pip install Homie3
~~~~


EG. To create a dimmer device requires that a set_dimmer method be provided. When creating a device, all that is required is to provide the MQTT settings. All other requirements of the Homie specification are automatically handled.

~~~~
import time

from homie.device_dimmer import Device_Dimmer

mqtt_settings = {
    'MQTT_BROKER' : 'QueenMQTT',
    'MQTT_PORT' : 1883,
}

class My_Dimmer(Device_Dimmer):

    def set_dimmer(self,percent):
        print('Received MQTT message to set the dimmer to {}. Must replace this method'.format(percent))
        super().set_dimmer(percent)        

try:

    dimmer = My_Dimmer(name = 'Test Dimmer',mqtt_settings=mqtt_settings)
    
    while True:
        dimmer.update_dimmer(0)
        time.sleep(5)
        dimmer.update_dimmer(50)
        time.sleep(5)
        dimmer.update_dimmer(100)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")      


~~~~

If creating multiple homie devices, you can specify Homie to only use one MQTT connection. This can be an issue on devices with limited resources. For MQTT_SETTINGS add MQTT_SHARE_CLIENT: True.
