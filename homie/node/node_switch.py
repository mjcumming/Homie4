from .node_base import Node_Base

from homie.node.property.property_switch import Property_Switch


class Node_Switch(Node_Base):
    def __init__(
        self,
        device,
        id="switch",
        name="Switch",
        type_="switch",
        retain=True,
        qos=1,
        set_switch=None,
    ):
        super().__init__(device, id, name, type_, retain, qos)

        assert set_switch  # must provide a function to set the value of the switch

        self.add_property(Property_Switch(self, set_value=set_switch))

    def update_switch(self, onoff):
        self.get_property("switch").value = onoff

