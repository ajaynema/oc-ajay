from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../yang-py"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from bgp import open
import pyangbind.lib.pybindJSON as pybindJSON

config = openconfig_bgp_global_config()
config.router_id = "1.1.1.1"
print(pybindJSON.dumps(config))

