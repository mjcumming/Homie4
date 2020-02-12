#!/usr/bin/env python

import logging
import netifaces
import socket

logger = logging.getLogger(__name__)

""" or use psutils

import psutil

mac_addresses = []

nics = psutil.net_if_addrs()
nics.pop('lo') # remove loopback since it doesnt have a real mac address

for i in nics:
    for j in nics[i]:
        if j.family == 17:  # AF_LINK
            mac_addresses.append(j.address)
"""


class Network_Information(object):
    """Util for getting a interface' ip to a specific host and the corresponding mac address."""

    def __init__(self):
        self.ip_to_interface = self.__build_ip_to_interface_dict()

    def __build_ip_to_interface_dict(self):
        """Build a map of IPv4-Address to Interface-Name (like 'eth0')"""
        map = {}
        for interface in netifaces.interfaces():
            try:
                ifInfo = netifaces.ifaddresses(interface)[netifaces.AF_INET]
                for addrInfo in ifInfo:
                    addr = addrInfo.get("addr")
                    if addr:
                        map[addr] = interface
            except Exception:
                pass
        return map

    def get_local_ip(self, targetHost, targetPort):
        """Gets the local ip to reach the given ip.
        That can be influenced by the system's routing table.
        A socket is opened and closed immediately to achieve that."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((targetHost, targetPort))
        except Exception as e:
            logger.exception(
                "Cannot create socket to target " + targetHost + ":" + targetPort
            )
        else:
            ip = s.getsockname()[0]
            s.close()
        return ip

    def get_local_mac_for_ip(self, ip):
        """Get the mac address for that given ip."""
        logger.debug("Interfaces found: %s", self.ip_to_interface)
        logger.debug("Looking for IP: %s", ip)

        mac_addr = None
        if_name = self.ip_to_interface.get(ip)

        try:
            link = netifaces.ifaddresses(if_name)[netifaces.AF_LINK]
        except (KeyError, TypeError):
            logger.warning("Could not determine MAC for: %s", if_name)
        else:
            logger.debug("Found link: %s", link)
            if len(link) > 1:
                logger.warning("Conflict: Multiple interfaces found for IP: %s!", ip)
            mac_addr = link[0].get("addr")
        return mac_addr

