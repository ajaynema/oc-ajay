from __future__ import print_function, unicode_literals

import os
import sys, os.path
YANG_PY_DIR = "../../../yang-py/openconfig"
sys.path.append(YANG_PY_DIR)
sys.path.append(".")

from local_routing import openconfig_local_routing
import pyangbind.lib.pybindJSON as pybindJSON

# Instantiate a copy of the pyangbind-kettle module
oclr = openconfig_local_routing()
print(oclr)

# Add an entry to the static route list
rt = oclr.local_routes.static_routes.static.add("192.0.2.1/32")

# Set a tag for the route
rt.config.set_tag = 42

# Retrieve the tag value
print(rt.config.set_tag)

# Retrieve the tag value through the original object
print(oclr.local_routes.static_routes.static["192.0.2.1/32"].config.set_tag)

# Use the get() method to see the content of the classes
# using the filter=True keyword to get only elements that
# are not empty or the default
print(oclr.local_routes.static_routes.static["192.0.2.1/32"].get(filter=True))

# Add a set of next_hops
for nhop in [(0, "192.168.0.1"), (1, "10.0.0.1")]:
    nh = rt.next_hops.next_hop.add(nhop[0])
    nh.config.next_hop = nhop[1]

# Iterate through the next-hops added
for index, nh in rt.next_hops.next_hop.iteritems():
    print("%s: %s" % (index, nh.config.next_hop))

# Try and set an invalid tag type
try:
    rt.config.set_tag = "INVALID-TAG"
except ValueError as m:
    print("Cannot set tag: %s" % m)

# Dump the entire instance as JSON in PyangBind format
print(pybindJSON.dumps(oclr))

# Dump the static routes instance as JSON in IETF format
print(pybindJSON.dumps(oclr.local_routes, mode="ietf"))