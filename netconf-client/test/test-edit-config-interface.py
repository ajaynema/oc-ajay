from ncclient import manager

m = manager.connect(host='localhost', port='17830', username='admin',
                    password='netconf', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)
rpc = '''<config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                    <name>eth0</name>
                    </interface>
                </interfaces>
        </config>
            '''

reply = m.edit_config(rpc, target='running')
print(reply)
reply=m.commit()
print(reply)

