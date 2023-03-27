import happybase as hb

# scan powers table
connection = hb.Connection('localhost')
connection.open()
powers = connection.table('powers')


for key, data in powers.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

