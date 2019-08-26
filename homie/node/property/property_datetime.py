from .property_base import Property_Base

import datetime

class Property_DateTime(Property_Base):

    def __init__(self, node, id, name, settable=False, retained=True, qos=1, unit=None, data_type='datetime', data_format=None, value=None, set_value=None):
        
        super().__init__(node,id,name,settable,retained,qos,unit,'datetime',data_format,value,set_value)

    def validate_value(self, value):
        try:
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
            return True
        except:
            return False

    def get_value_from_payload(self,payload):
        try:
            return datetime.datetime.strptime(payload, '%Y-%m-%d %H:%M:%S.%f')
        except:
            return None
    


