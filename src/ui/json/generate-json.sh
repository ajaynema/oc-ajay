mkdir -p openconfig
cd openconfig    
YANGDIR=../../../yang
pyang  -f jtox  -o system.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/system/openconfig-system.yang
pyang  -f jtox  -o platform.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/platform/openconfig-platform.yang
pyang  -f jtox  -o network-instance.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/network-instance/openconfig-network-instance.yang