from .node_base import Node_Base

from homie.node.property.property_boolean import Property_Boolean


class Node_Boolean(Node_Base):
    def __init__(
        self,
        device,
        id="boolean",
        name="Boolean",
        type_="boolean",
        retain=True,
        qos=1,
        set_boolean=None,
    ):
        super().__init__(device, id, name, type_, retain, qos)

        assert set_boolean  # must provide a function to set the value of the switch

        self.add_property(Property_Boolean(self, set_value=set_boolean))

    def update_boolean(self, boolean):
        self.get_property("boolean").value = boolean

