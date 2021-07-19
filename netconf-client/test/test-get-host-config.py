from ncclient import manager

m = manager.connect(host='localhost', port='17830', username='admin',
                    password='netconf', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)

int_filter = '''
                <hostname>
                </hostname>
                '''

# get-config RPC against the running datastore using a subtree filter
reply = m.get_config('running', filter=('subtree', int_filter))

# Print RPC reply
print(reply)


