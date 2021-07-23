from ncclient import manager

m = manager.connect(host='localhost', port='11002', username='root',
                    password='root', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)
reply = m.get_config('running')
# Print RPC reply
print(reply)

