export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`
mkdir -p yang-py
cd yang-py
YANGDIR=../yang
echo "generating acl..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o local_routing.py  -p $YANGDIR/models $YANGDIR/models/local-routing/*.yang
echo "successfully generated python classes for yang files ..."


#pyang --plugindir $PYBINDPLUGIN -f pybind --split-class-dir -o bgp.py ../../yang/models/bgp/openconfig-bgp.yang ../../yang/models/rib/openconfig-rib-bgp.yang ../../yang/models/bgp/openconfig-bgp-common-multiprotocol.yang ../../yang/models/bgp/openconfig-bgp-types.yang ../../yang/models/openconfig-extensions.yang ../../yang/models/types/openconfig-inet-types.yang ../../yang/models/types/openconfig-yang-types.yang ../../yang/models/types/openconfig-types.yang
