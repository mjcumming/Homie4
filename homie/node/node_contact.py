from .node_base import Node_Base

from homie.node.property.property_contact import Property_Contact


class Node_Contact(Node_Base):
    def __init__(
        self, device, id="contact", name="Contact", type_="contact", retain=True, qos=1
    ):
        super().__init__(device, id, name, type_, retain, qos)

        self.add_property(Property_Contact(self, "contact"))

    def update_contact(self, contact):
        self.get_property("contact").value = contact

