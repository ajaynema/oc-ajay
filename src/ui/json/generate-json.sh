mkdir -p openconfig
cd openconfig    
YANGDIR=../../../yang
pyang  -f jtox  -o system.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/system/openconfig-system.yang
pyang  -f jtox  -o platform.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/platform/openconfig-platform.yang
pyang  -f jtox  -o network-instances.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/network-instance/openconfig-network-instance.yang
pyang  -f jtox  -o terminal-device.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/optical-transport/openconfig-terminal-device.yang
pyang  -f jtox  -o isis.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/isis/openconfig-isis.yang