from ncclient import manager

m = manager.connect(host='localhost', port='17830', username='admin',
                    password='netconf', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)
rpc = '''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <hostname xmlns="urn:opendaylight:hostname">
                <system>
                    <hostname>
                        test
                    </hostname>
                    <location>
                        test-location
                    </location>
                </system>
            </hostname>
        </config>
            '''

reply = m.edit_config(rpc, target='running')
print(reply)
reply=m.commit()
print(reply)

