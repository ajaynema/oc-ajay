from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../../yang-py/openconfig"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from system import openconfig_system
import pyangbind.lib.pybindJSON as pybindJSON
ocs = openconfig_system()
ocs.system.config.hostname = "test"
ocs.system.config.domain_name = "test"
print(pybindJSON.dumps(ocs))