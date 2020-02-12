#!/usr/bin/env python

import time

from homie.device_thermostat import Device_Thermostat

mqtt_settings = {
    "MQTT_BROKER": "openhab",
    "MQTT_PORT": 1883,
}

THERMOSTAT_SETTINGS = {
    "current_temperature": 70,
    "current_humidity": 30,
    "cool_setpoint": 70,
    "max_cool_setpoint": 90,
    "min_cool_setpoint": 60,
    "heat_setpoint": 70,
    "max_heat_setpoint": 90,
    "min_heat_setpoint": 60,
    "fan_mode": "ON",
    "fan_modes": ["ON", "AUTO"],
    "hold_mode": "SCHEDULE",
    "hold_modes": ["SCHEDULE", "TEMPORARY", "PERMANENT"],
    "system_mode": "OFF",
    "system_modes": ["OFF", "HEAT", "COOL", "AUTO"],
    "system_status": "OFF",
    "units": "F",
}


try:

    therm = Device_Thermostat(
        name="Thermostat",
        mqtt_settings=mqtt_settings,
        thermostat_settings=THERMOSTAT_SETTINGS,
    )

    while True:
        therm.update_current_temperature(60)
        therm.update_current_humidity(10)
        therm.update_heat_setpoint(70)
        therm.update_cool_setpoint(80)
        time.sleep(5)
        therm.update_current_temperature(66)
        therm.update_current_humidity(30)
        therm.update_heat_setpoint(75)
        therm.update_cool_setpoint(85)
        time.sleep(5)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
