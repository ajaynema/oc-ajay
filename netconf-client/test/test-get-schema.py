from ncclient import manager

m = manager.connect(host='localhost', port='17830', username='admin',
                    password='netconf', device_params={'name':'iosxe'}, hostkey_verify=False)
print(m.connected)
schema = m.get_schema('test',"2014-10-17")
print(schema)
schema = m.get_schema('hostname',"2017-03-31")
print(schema)