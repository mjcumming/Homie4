from homie.node.property.property_float import Property_Float

class Property_Pressure(Property_Float):
    def __init__(
        self,
        node,
        id="pressure",
        name="Pressure",
        settable=False,
        retained=True,
        qos=1,
        unit="Pa",
        data_type=None,
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
            data_type,
            data_format,
            value,
            set_value,
            tags,
            meta,
        )
