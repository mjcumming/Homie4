from homie.support.helpers import validate_id


class Node_Base(object):
    def __init__(self, device, id, name, type_, retain=True, qos=1):
        assert validate_id(id), "Node ID {} is not valid".format(id)
        assert device

        self.id = id
        self.name = name
        self.type = type_
        self.device = device

        self.retain = retain
        self.qos = qos

        self.properties = {}

        self.topic = self.device.topic

        self.published = False

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, parent_topic):
        self._topic = "/".join([parent_topic, self.id])

    def add_property(self, property_):
        # assert self.properties [property_.id] == None
        assert property_.id not in self.properties

        self.properties[property_.id] = property_

        if self.published:  # need to update publish property changes
            self.publish_properties()

    def remove_property(self, property_id):
        property_ = self.properties[property_id]
        del self.properties[property_id]

        if self.device.start_time is not None:  # running, publish property changes
            self.publish_properties()
            property_.publish_attributes(False, 1)

    def get_property(self, property_id):
        if property_id in self.properties:
            return self.properties[property_id]
        else:
            return None

    def set_property_value(self, property_id, value):
        self.get_property(property_id).value = value

    def publish(self, topic, payload, retain, qos):
        self.device.publish(topic, payload, retain, qos)

    def property_publisher(
        self, topic, payload, retain, qos
    ):  # properties use this to publish
        if self.published:  # only publish if the node has been published
            self.device.publish(topic, payload, retain, qos)

    def publish_attributes(self, retain=True, qos=1):
        self.publish("/".join((self.topic, "$name")), self.name, retain, qos)
        self.publish("/".join((self.topic, "$type")), self.type, retain, qos)

        self.publish_properties()

    def publish_properties(self, retain=True, qos=1):
        properties = ",".join(self.properties.keys())
        self.publish("/".join((self.topic, "$properties")), properties, retain, qos)

        self.published = True  # node basics published

        for _, property_ in self.properties.items():
            # print ('NODE PUBLISH PROP ',property_.name)
            property_.publish_attributes(retain, qos)

    def get_subscriptions(self):
        subscriptions = {}

        for _, property_ in self.properties.items():
            subscriptions.update(property_.get_subscriptions())

        return subscriptions

