from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../yang-py"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")
import system 
import pyangbind.lib.pybindJSON as pybindJSON
new_ocs = pybindJSON.load(os.path.join(".", "ntp.json"), system, "openconfig_system")
print(pybindJSON.dumps(new_ocs))