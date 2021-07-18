from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../../yang-py/openconfig"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from bgp import openconfig_bgp
import pyangbind.lib.pybindJSON as pybindJSON

bgp = openconfig_bgp()
#gp.global_.config.as_ = 2856
#bgp.global_.config.router_id = "1.1.1.1"

print(pybindJSON.dumps(bgp.obj))