from .property_base import Property_Base


class Property_String(Property_Base):
    def __init__(
        self,
        node,
        id,
        name,
        settable=False,
        retained=True,
        qos=1,
        unit=None,
        data_type="string",
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
            "string",
            data_format,
            value,
            set_value,
            tags,
            meta,
        )

