from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../../yang-py/openconfig"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from system import openconfig_system
import pyangbind.lib.pybindJSON as pybindJSON
ocs = openconfig_system()
ocs.system.dns.servers.server.add(0)
server = ocs.system.dns.servers.server[0]
server.config.address = "1.1.1.1"
print(pybindJSON.dumps(server))
print(pybindJSON.dumps(ocs))