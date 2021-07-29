mkdir -p openconfig
cd openconfig    
YANGDIR=../../../yang
pyang  -f jtox  -o system.json   -p $YANGDIR/models/openconfig $YANGDIR/models/openconfig/system/openconfig-system.yang