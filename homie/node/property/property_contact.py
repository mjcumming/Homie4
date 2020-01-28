from .property_boolean import Property_Boolean


tags = ["Contact"]


class Property_Contact(Property_Boolean):
    def __init__(
        self,
        node,
        id="contact",
        name="Contact",
        settable=False,
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
        return value in ["OPEN", "CLOSED"]

    def get_payload_from_value(self, value):
        if value == "OPEN":
            return "true"
        else:
            return "false"


"""
from .property_enum import Property_Enum

class Property_Contact(Property_Enum):

    def __init__(self, node, id='contact', name='Contact', settable=False, retained=False, qos=1, unit=None, data_type='enum', data_format='OPEN,CLOSED', value=None, set_value=None, tags=[], meta={}):
        
        super().__init__(node, id,name,settable,retained,qos,unit,data_type,data_format,value,set_value)

 """
