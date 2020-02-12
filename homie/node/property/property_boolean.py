from .property_base import Property_Base


class Property_Boolean(Property_Base):
    def __init__(
        self,
        node,
        id="boolean",
        name="Boolean",
        settable=True,
        retained=True,
        qos=1,
        unit=None,
        data_type="boolean",
        data_format=None,
        value=None,
        set_value=None,
        tags=[],
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
            "boolean",
            data_format,
            value,
            set_value,
            tags,
            meta,
        )

    def validate_value(self, value):
        return isinstance(value, bool)

    def get_value_from_payload(self, payload):
        if payload == "true":
            return True
        elif payload == "false":
            return False
        else:
            return None

    def get_payload_from_value(self, value):  # convert value to a payload for homie
        return value and "true" or "false"

