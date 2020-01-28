from .property_boolean import Property_Boolean


tags = ["Switch"]


class Property_Switch(Property_Boolean):
    def __init__(
        self,
        node,
        id="switch",
        name="Switch",
        settable=True,
        retained=True,
        qos=1,
        unit=None,
        data_type=None,
        data_format=None,
        value=None,
        set_value=None,
        tags=tags,
        meta={},
    ):
        super().__init__(
            node,
            id,
            name,
            settable,
            retained,
            qos,
            unit,
            data_type,
            data_format,
            value,
            set_value,
            tags,
            meta,
        )

    def validate_value(self, value):
        return value in ["ON", "OFF"]

    def get_value_from_payload(self, payload):
        if payload == "true":
            return "ON"
        elif payload == "false":
            return "OFF"
        else:
            return None

    def get_payload_from_value(self, value):
        if value == "ON":
            return "true"
        else:
            return "false"

