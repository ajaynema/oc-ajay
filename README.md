# oc-nlp-ajay - NLP Interface to networking device using YANG.

Project to play with AI/ML, openconfig and yang and learn the python and yang.
Same time trying to make tool useful for automation and telecom and networking programmers. 

Fun:

1.  Understand the open config yang file - Done
2.  Generate the python classes - Done
3.  Use the python classes to generate the payload - Done
4.  Load the classes from json payload - Done
5.  Run Simulator
6.  set and get from simulator using netconf client
7.  set and get from simulator using  gRPC
8.  Notification from simulator
9.  Performance data from simulator
10. Dynamic UI from Yang Files
11. Data Storage for data
12. Device management - "Low-Code"
13. NLP Interface to YANG Interface



# Commands
export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`


# Packages
pip install pyyang
pip install pyyangbind

# Peferences

https://rob.sh/post/209/
http://yang.ciscolive.com/pod0/labs/lab9/lab9-m6
https://developer.cisco.com/docs/openconfig-yang-release-9-2x/#oc-acl/querying-an-ipv4-acl-policy1
https://gist.github.com/robshakir/c4221228b209e0abe847
https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-1775.pdf
http://ydk.cisco.com/py/docs/gen_doc_ab7a308aaa0f3c83ee97d51af7c340f088f28655.html
https://pc.nanog.org/static/published/meetings/NANOG71/1456/20171003_Alvarez_Getting_Started_With_v1.pdf
https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang
