from __future__ import print_function, unicode_literals

import os
import sys, os.path

sys.path.append("../yang-py")

sys.path.append("..")

import local_routes

import pyangbind.lib.pybindJSON as pybindJSON

# Instantiate a copy of the pyangbind-kettle module
local_routes = local_routes()

# Add an entry to the static route list
rt = local_routes.static_routes.static.add("192.0.2.1/32")

# Set a tag for the route
rt.config.set_tag = 42

# Retrieve the tag value
print(rt.config.set_tag)

print(pybindJSON.dumps(local_routes))

# Dump the static routes instance as JSON in IETF format
print(pybindJSON.dumps(oclr.local_routes, mode="ietf"))

# Load the "json/oc-lr.json" file into a new instance of
# "openconfig_local_routing". We import the module here, such that a new
# instance of the class can be created by the deserialisation code
import binding

new_oclr = pybindJSON.load(os.path.join("json", "oc-lr.json"), binding, "openconfig_local_routing")

# Manipulate the data loaded
print("Current tag: %d" % new_oclr.local_routes.static_routes.static["192.0.2.1/32"].config.set_tag)
new_oclr.local_routes.static_routes.static["192.0.2.1/32"].config.set_tag += 1
print("New tag: %d" % new_oclr.local_routes.static_routes.static["192.0.2.1/32"].config.set_tag)

# Load JSON into an existing class structure
from pyangbind.lib.serialise import pybindJSONDecoder
import json

ietf_json = json.load(open(os.path.join("json", "oc-lr_ietf.json"), "r"))
pybindJSONDecoder.load_ietf_json(ietf_json, None, None, obj=new_oclr.local_routes)

# Iterate through the classes - both the 192.0.2.1/32 prefix and 192.0.2.2/32
# prefix are now in the objects
for prefix, route in new_oclr.local_routes.static_routes.static.iteritems():
    print("Prefix: %s, tag: %d" % (prefix, route.config.set_tag))