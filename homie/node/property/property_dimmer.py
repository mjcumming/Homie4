from .property_integer import Property_Integer

tags = ["Lighting", "Dimmable"]


class Property_Dimmer(Property_Integer):
    def __init__(
        self,
        node,
        id="dimmer",
        name="Dimmer",
        settable=True,
        retained=True,
        qos=1,
        unit="%",
        data_type=None,
        data_format="0:100",
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

