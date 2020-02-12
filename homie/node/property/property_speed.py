import logging
from .property_enum import Property_Enum

logger = logging.getLogger(__name__)


class Property_Speed(Property_Enum):
    def __init__(
        self,
        node,
        id="speed",
        name="Speed",
        settable=True,
        retained=True,
        qos=1,
        unit=None,
        data_type="enum",
        data_format="OFF,LOW,MEDIUM,HIGH",
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

