import re


"""'

Topic IDs

An MQTT topic consists of one or more topic levels, separated by the slash character (/). A topic level ID MAY contain lowercase letters from a to z, numbers from 0 to 9 as well as the hyphen character (-).
A topic level ID MUST NOT start or end with a hyphen (-). The special character $ is used and reserved for Homie attributes. The underscore (_) is used and reserved for Homie node arrays.

"""


def validate_id(id):
    if isinstance(id, str):
        r = re.compile("(^(?!\-)[a-z0-9\-]+(?<!\-)$)")
        return id if r.match(id) else False


if __name__ == "__main__":

    print(validate_id("Xx"))
    print(validate_id(3368967))
