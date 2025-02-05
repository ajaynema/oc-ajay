# Tech Learn Series

## oc-nlp-ajay - Open config UI and NLP Interface and integration with TMF Bussiness model for automation and monitoring for networking device using YANG.

Project is tech fun and learn series to learn the **python**, **YANG**, **gRPC**, **gNMI**, **NETCONF**, **TMF APIs** and **AI/ML**. 
Same time trying to make useful **tools** and **framework for automation and monitoring** for **networking devices** for **telecom** and **networking programmers**. 

### Learning Track:

####    DONE:

**=>  Understand the open config yang file - Done**

**=>  Generate the python classes - Done**

**=>  Use the python classes to generate the payload - Done**

**=>  Load the classes from json payload - Done**

**=>  Run Simulator - Done**

**=>  netconf client (connect and get capabilites) - Done**

**=>  netconf client (connect and get schemas) - Done**

####    Pending:

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

## TMF Standard Implementation

=> [TMF642 - Alarm Management Implementation - Done](https://github.com/ajaynema/oc-nlp-ajay/blob/main/src/tmf/tmf642/Readme.md)

=> [TMF639 - Resource Inventory Management Implementation - Done](https://github.com/ajaynema/oc-nlp-ajay/blob/main/src/tmf/tmf639/Readme.md)

=> [TMF620 - Product Catalog Management - ]

=> [TMF621 - Trouble Ticket  - ]

=> [TMF629 - Customer Management - ]

=> [TMF632 - Party Management - ]

=> [TMF633 - Service Catalog - ]

=> [TMF635 - Usage Management - ]

=> [TMF637 - Product Inventory Management - ]

=> [TMF640 - Service activation Management - ]

=> [TMF645 - Service qualification Management - ]

=> [TMF646 - Appointment - ]

=> [TMF648 - Quote Management - ]

=> [TMF6451 - Agreement Management]

=> [TMF640 - Service activation Management - ]

## Packages

pip install pyyang

pip install pyyangbind

pip install ncclient

pip install -U paramiko 

pip install flask

pip install jsonpickle

pip install pymongo

pip install requests

pip install rasa

## Commands
export PYBINDPLUGIN=`/usr/bin/env python -c 'import pyangbind; import os; print("%s/plugin" % os.path.dirname(pyangbind.__file__))'`

## References and URLs 

https://rob.sh/post/209/
http://yang.ciscolive.com/pod0/labs/lab9/lab9-m6
https://developer.cisco.com/docs/openconfig-yang-release-9-2x/#oc-acl/querying-an-ipv4-acl-policy1
https://gist.github.com/robshakir/c4221228b209e0abe847
https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2017/pdf/DEVNET-1775.pdf
http://ydk.cisco.com/py/docs/gen_doc_ab7a308aaa0f3c83ee97d51af7c340f088f28655.html
https://pc.nanog.org/static/published/meetings/NANOG71/1456/20171003_Alvarez_Getting_Started_With_v1.pdf
https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang
https://docs.opendaylight.org/projects/netconf/en/latest/testtool.html#verifying-testtool
https://github.com/CiscoDevNet/ncc
https://pubhub.devnetcloud.com/media/yang-connector/docs/README.html
https://pypi.org/project/pyats/
https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2019/pdf/BRKDEV-1368.pdf
https://www.netacad.com/sites/default/files/images/careers/Webinars/DevNet/devnet_session_7_networkprogrammability_yang_netconf_restconf.pdf
https://pythonhosted.org/an_example_pypi_project/setuptools.html
https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html

### GRPC
https://github.com/openconfig/public/blob/master/doc/oc_by_example.md
