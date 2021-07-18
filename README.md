# Fun and Learn Tech Series with Ajay

# oc-nlp-ajay - Open config UI and NLP Interface and integration with TMF Bussiness model for automation and monitoring for networking device using YANG.

Project is tech fun and learn series by Ajay to learn the **python**, **YANG**, **gRPC**, **gNMI**, **NETCONF**, **TMF APIs** and **AI/ML**. 
Same time trying to make useful **tools** and **framework for automation and monitoring** for **networking devices** for **telecom** and **networking programmers**. 

# Fun activities:

#    DONE:

**=>  Understand the open config yang file - Done**

**=>  Generate the python classes - Done**

**=>  Use the python classes to generate the payload - Done**

**=>  Load the classes from json payload - Done**

**=>  Run Simulator - Done**

**=>  netconf client (connect and get capabilites) - Done**

**=>  netconf client (connect and get schemas) - Done**

#    Pending:

=>  set and get from simulator using netconf client

=>  set and get from simulator using  gRPC

=>  Notification from simulator

=>  Performance data from simulator

=> Dynamic UI from Yang Files

=> Data Storage for device configuration

=> Device management - "Low-Code"

=> NLP Interface to YANG Interface

=> Templete based configuration

=> TMF interface for open config

=> BPMN workflow engine for automation

=> Docker image for easy to deploy and use.


# Packages

pip install pyyang

pip install pyyangbind

pip install ncclient

pip install -U paramiko 

# Commands
export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`

# References and URLs 

https://rob.sh/post/209/
http://yang.ciscolive.com/pod0/labs/lab9/lab9-m6
https://developer.cisco.com/docs/openconfig-yang-release-9-2x/#oc-acl/querying-an-ipv4-acl-policy1
https://gist.github.com/robshakir/c4221228b209e0abe847
https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-1775.pdf
http://ydk.cisco.com/py/docs/gen_doc_ab7a308aaa0f3c83ee97d51af7c340f088f28655.html
https://pc.nanog.org/static/published/meetings/NANOG71/1456/20171003_Alvarez_Getting_Started_With_v1.pdf
https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang
https://docs.opendaylight.org/projects/netconf/en/latest/testtool.html#verifying-testtool
