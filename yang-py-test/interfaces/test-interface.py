from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../yang-py"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from interfaces import openconfig_interfaces
import pyangbind.lib.pybindJSON as pybindJSON

# Instantiate a copy of the pyangbind-kettle module
oci = openconfig_interfaces()
oci.interfaces.interface.add("eth0")
print(pybindJSON.dumps(oci))
eth0 = oci.interfaces.interface["eth0"]

eth0.config.description = "Linux eth0 interface"
eth0.config.enabled = "True"
eth0.ethernet.config.duplex_mode = "FULL"
eth0.ethernet.config.auto_negotiate = "True"

eth0.subinterfaces.subinterface.add(0)
subint0 = eth0.subinterfaces.subinterface[0]
subint0.config.description = "Primary public IP address"
subint0.config.enabled = "True"
#subint0.ipv4.address.add("192.0.2.1")
#subint0.ipv4.address["192.0.2.1"].config.prefix_length = 24

# Serialise the entire object
print(pybindJSON.dumps(oci))