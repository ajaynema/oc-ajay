from ncclient import manager

m = manager.connect(host='localhost', port='17830', username='admin',
                    password='netconf', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)
reply = m.get_config('running')
# Print RPC reply
print(reply)

