field_name="/state/key"
if field_name.startswith("/"):
    field_name = field_name[1:]
field_name = field_name.replace('/','.')
print(field_name)