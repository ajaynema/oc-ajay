export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`
mkdir -p yang-py
cd yang-py
YANGDIR=../yang
echo "generating acl..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o acl.py   -p $YANGDIR/models $YANGDIR/models/acl/*.yang
echo "generating aft..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o aft.py  -p $YANGDIR/models $YANGDIR/models/aft/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o bfd.py  -p $YANGDIR/models $YANGDIR/models/bfd/*.yang
echo "generating bgp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o bgp.py -p $YANGDIR/models $YANGDIR/models/bgp/*.yang
echo "generating catalog..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o catalog.py -p $YANGDIR/models $YANGDIR/models/catalog/*.yang
echo "generating extensions..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o extensions.py  -p $YANGDIR/models $YANGDIR/models/extensions/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o firewall.py  -p $YANGDIR/models $YANGDIR/models/firewall/*.yang
echo "generating interfaces..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o interfaces.py  -p $YANGDIR/models $YANGDIR/models/interfaces/*.yang
echo "generating isis..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o isis.py  -p $YANGDIR/models $YANGDIR/models/isis/*.yang
echo "generating lacp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o lacp.py  -p $YANGDIR/models $YANGDIR/models/lacp/*.yang
echo "generating lldp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o lldp.py  -p $YANGDIR/models $YANGDIR/models/lldp/*.yang
echo "generating local-routing..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o local_routing.py  -p $YANGDIR/models $YANGDIR/models/local-routing/*.yang
echo "generating macsec..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o macsec.py  -p $YANGDIR/models $YANGDIR/models/macsec/*.yang
echo "generating mpls..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o macsec.py  -p $YANGDIR/models $YANGDIR/models/macsec/*.yang
echo "generating multicast..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o multicast.py -p $YANGDIR/models $YANGDIR/models/multicast/*.yang
echo "generating network-instance..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o network_instance.py  -p $YANGDIR/models $YANGDIR/models/network-instance/*.yang
echo "generating openflow..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o openflow.py  -p $YANGDIR/models $YANGDIR/models/openflow/*.yang
echo "generating ...optical-transport"
pyang --plugindir $PYBINDPLUGIN -f  pybind -o optical_transport.py  -p $YANGDIR/models $YANGDIR/models/optical-transport/*.yang
echo "generating ospf..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o ospf.py  -p $YANGDIR/models $YANGDIR/models/ospf/*.yang
echo "generating p4rt..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o p4rt.py  -p $YANGDIR/models $YANGDIR/models/p4rt/*.yang
echo "generating platform..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o platform.py  -p $YANGDIR/models $YANGDIR/models/platform/*.yang
echo "generating policy..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o policy.py  -p $YANGDIR/models $YANGDIR/models/policy/*.yang
echo "generating policy-forwarding..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o policy_forwarding.py  -p $YANGDIR/models $YANGDIR/models/policy-forwarding/*.yang
echo "generating bfd..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o probes.py -p $YANGDIR/models $YANGDIR/models/probes/*.yang
echo "generating qos..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o qos.py  -p $YANGDIR/models $YANGDIR/models/qos/*.yang
echo "generating relay-agent..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o relay_agent.py  -p $YANGDIR/models $YANGDIR/models/relay-agent/*.yang
echo "generating rib..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o rib.py  -p $YANGDIR/models $YANGDIR/models/rib/*.yang
echo "generating sampling..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o sampling.py  -p $YANGDIR/models $YANGDIR/models/sampling/*.yang
echo "generating segment-routing..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o segment_routing.py  -p $YANGDIR/models $YANGDIR/models/segment-routing/*.yang
echo "generating stp..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o stp.py  -p $YANGDIR/models $YANGDIR/models/stp/*.yang
echo "generating system..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o system.py -p $YANGDIR/models $YANGDIR/models/system/*.yang
echo "generating telemetry..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o telemetry.py -p $YANGDIR/models $YANGDIR/models/telemetry/*.yang
echo "generating types..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o types.py  -p $YANGDIR/models $YANGDIR/models/types/*.yang
echo "generating vlan..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o vlan.py  -p $YANGDIR/models $YANGDIR/models/vlan/*.yang
echo "generating wifi..."
pyang --plugindir $PYBINDPLUGIN -f  pybind -o wifi.py  -p $YANGDIR/models $YANGDIR/models/wifi/*.yang
echo "successfully generated python classes for yang files ..."


#pyang --plugindir $PYBINDPLUGIN -f pybind --split-class-dir -o bgp.py ../../yang/models/bgp/openconfig-bgp.yang ../../yang/models/rib/openconfig-rib-bgp.yang ../../yang/models/bgp/openconfig-bgp-common-multiprotocol.yang ../../yang/models/bgp/openconfig-bgp-types.yang ../../yang/models/openconfig-extensions.yang ../../yang/models/types/openconfig-inet-types.yang ../../yang/models/types/openconfig-yang-types.yang ../../yang/models/types/openconfig-types.yang
