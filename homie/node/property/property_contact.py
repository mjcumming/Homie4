from .property_enum import Property_Enum

class Property_Contact(Property_Enum):

    def __init__(self, node, id='contact', name='Contact', settable=False, retained=False, qos=1, unit=None, data_type='enum', data_format='OPEN,CLOSED', value=None, set_value=None):
        
        super().__init__(node, id,name,settable,retained,qos,unit,data_type,data_format,value,set_value)

 

