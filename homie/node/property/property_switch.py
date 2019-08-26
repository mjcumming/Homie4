from .property_enum import Property_Enum


tags = ['Switch']


class Property_Switch(Property_Enum):

    def __init__(self, node, id='switch', name = 'Switch', settable = True, retained = True, qos=1, unit = None, data_type= 'enum', data_format = 'ON,OFF', value = None, set_value=None, tags=tags, meta=None):
        
        super().__init__(node,id,name,settable,retained,qos,unit,data_type,data_format,value,set_value,tags,meta)

 

