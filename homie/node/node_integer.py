from .node_base import Node_Base

from homie.node.property.property_integer import Property_Integer


class Node_Integer(Node_Base):
    def __init__(
        self,
        device,
        id="integer",
        name="State",
        type_="integer",
        retain=True,
        qos=1,
        set_value=None,
    ):
        super().__init__(device, id, name, type_, retain, qos)

        assert set_value

        self.add_property(
            Property_Integer(self, "integer", "Integer", set_value=set_value)
        )

    def update_value(self, value):
        self.get_property("integer").value = value

