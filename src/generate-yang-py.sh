export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`
mkdir -p yang-py
cd yang-py
mkdir -p openconfig
cd openconfig    
YANGDIR=../../yang
echo "generating acl..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o acl.py   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/acl/*.yang
echo "generating aft..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o aft.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/aft/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o bfd.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/bfd/*.yang
echo "generating bgp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o bgp.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/bgp/*.yang
echo "generating catalog..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o catalog.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/catalog/*.yang
echo "generating extensions..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o extensions.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/extensions/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o firewall.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/firewall/*.yang
echo "generating interfaces..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o interfaces.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/interfaces/*.yang
echo "generating isis..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o isis.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/isis/*.yang
echo "generating lacp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o lacp.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/lacp/*.yang
echo "generating lldp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o lldp.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/lldp/*.yang
echo "generating local-routing..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o local_routing.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/local-routing/*.yang
echo "generating macsec..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o macsec.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/macsec/*.yang
echo "generating mpls..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o macsec.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/macsec/*.yang
echo "generating multicast..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o multicast.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/multicast/*.yang
echo "generating network-instance..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o network_instance.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/network-instance/*.yang
echo "generating openflow..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o openflow.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/openflow/*.yang
echo "generating ...optical-transport"
pyang --plugindir $PYBINDPLUGIN -f  pybind -o optical_transport.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/optical-transport/*.yang
echo "generating ospf..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o ospf.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/ospf/*.yang
echo "generating p4rt..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o p4rt.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/p4rt/*.yang
echo "generating platform..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o platform.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/platform/*.yang
echo "generating policy..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o policy.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/policy/*.yang
echo "generating policy-forwarding..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o policy_forwarding.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/policy-forwarding/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o probes.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/probes/*.yang
echo "generating qos..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o qos.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/qos/*.yang
echo "generating relay-agent..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o relay_agent.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/relay-agent/*.yang
echo "generating rib..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o rib.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/rib/*.yang
echo "generating sampling..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o sampling.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/sampling/*.yang
echo "generating segment-routing..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o segment_routing.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/segment-routing/*.yang
echo "generating stp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o stp.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/stp/*.yang
echo "generating system..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o system.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/system/*.yang
echo "generating telemetry..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o telemetry.py -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/telemetry/*.yang
echo "generating types..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o types.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/types/*.yang
echo "generating vlan..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o vlan.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/vlan/*.yang
echo "generating wifi..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o wifi.py  -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/wifi/*.yang
echo "successfully generated python classes for yang files ..."


#pyang --plugindir $PYBINDPLUGIN -f pybind --split-class-dir -o bgp.py ../../yang/models/openconfig/bgp/openconfig-bgp.yang ../../yang/models/openconfig/rib/openconfig-rib-bgp.yang ../../yang/models/openconfig/bgp/openconfig-bgp-common-multiprotocol.yang ../../yang/models/openconfig/bgp/openconfig-bgp-types.yang ../../yang/models/openconfig/openconfig-extensions.yang ../../yang/models/openconfig/types/openconfig-inet-types.yang ../../yang/models/openconfig/types/openconfig-yang-types.yang ../../yang/models/openconfig/types/openconfig-types.yang
