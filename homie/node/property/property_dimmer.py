from .property_float import Property_Float

tags = ['Lighting','Dimmable']

class Property_Dimmer(Property_Float):

    def __init__(self,node, id='dimmer', name = 'Dimmer', settable = True, retained = True, qos=1, unit = '%', data_type= None, data_format = '0:100', value = None, set_value=None, tags=tags, meta={}):
        
        super().__init__(node,id,name,settable,retained,qos,unit,data_type,data_format,value,set_value,tags,meta)

    def get_value_from_payload(self,payload):
        try:
            return round(float(payload)*100)
        except:
            return None

    def get_payload_from_value(self,value): 
        try:
            return round(value/100,2)
        except:
            return None

'''
from .property_integer import Property_Integer

tags = ['Lighting','Dimmable']

class Property_Dimmer(Property_Integer):

    def __init__(self,node, id='dimmer', name = 'Dimmer', settable = True, retained = True, qos=1, unit = '%', data_type= None, data_format = '0:100', value = None, set_value=None, tags=tags, meta={}):
        
        super().__init__(node,id,name,settable,retained,qos,unit,data_type,data_format,value,set_value,tags,meta)
'''