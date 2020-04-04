# Homie

Python 3 implementation of Homie 4.0.0

Class based system to easily add Homie 4.0.0 support to devices.

Supports the Meta, Statistics, and Firmware extensions

Includes ready to use common devices such as switch, dimmer, contact, thermostat, boolean, etc. 

**Install**

~~~~
pip install Homie4
~~~~

Note: On Raspbian use 

~~~~
pip3 install Homie4
~~~~

**Temperature Probe Example**

Creates a temperature device using a AM2302 sensor. 

~~~~python
import Adafruit_DHT
import time

from homie.device_temperature import Device_Temperature

mqtt_settings = {
    'MQTT_BROKER' : 'OpenHAB',
    'MQTT_PORT' : 1883,
}

try:

    temperature_device = Device_Temperature(device_id="temperature-sensor-1",name = "Temperature_Sensor 1",mqtt_settings=mqtt_settings)
    sensor = Adafruit_DHT.AM2302
    pin = 4

    
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print(temperature)
        temperature_device.update_temperature(temperature)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")   
~~~~


**Dimmer Example** 

To create a dimmer device requires that a set_dimmer method be provided. When creating a device, all that is required is to provide the MQTT settings. All other requirements of the Homie specification are automatically handled.

```python
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


````



If creating multiple homie devices, you can specify Homie to only use one MQTT connection. This can be an issue on devices with limited resources. For MQTT_SETTINGS add MQTT_SHARE_CLIENT: True.
