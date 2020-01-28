from .node_base import Node_Base

from homie.node.property.property_dimmer import Property_Dimmer


class Node_Dimmer(Node_Base):
    def __init__(
        self,
        device,
        id="dimmer",
        name="Dimmer",
        type_="dimmer",
        retain=True,
        qos=1,
        set_dimmer=None,
    ):
        super().__init__(device, id, name, type_, retain, qos)

        assert set_dimmer  # must provide a function to set the value of the dimmer

        self.add_property(Property_Dimmer(self, set_value=set_dimmer))

    def update_dimmer(self, percent):
        self.get_property("dimmer").value = percent

