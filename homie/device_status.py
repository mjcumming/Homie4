from homie.device_base import Device_Base
from homie.node.node_base import Node_Base


class Device_Status(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):

        super().__init__(device_id, name, homie_settings, mqtt_settings)

        node = Node_Base(self, "status", "Status", "status")
        self.add_node(node)

        self.register_status_properties(node)

        self.start()

    def register_status_properties(self, node):
        raise RuntimeError("Override in subclass")

