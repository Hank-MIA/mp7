import happybase as hb

# Connect to the database
connection = hb.Connection('localhost')
connection.open()

powers = connection.table('powers')

# read hero, power, name, xp, color from row1 in the powers table
row = powers.row(b'row1', columns=[b'personal:hero', b'personal:power', b'professional:name', b'professional:xp', b'custom:color'])
print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(
    row[b'personal:hero'], row[b'personal:power'], row[b'professional:name'], row[b'professional:xp'], row[b'custom:color'])
)

# read hero and color from row19 in the powers table
row = powers.row(b'row19', columns=[b'personal:hero', b'custom:color'])
print('hero: {}, color: {}'.format(row[b'personal:hero'], row[b'custom:color']))

# read hero, name and color from row1 in the powers table
row = powers.row(b'row1', columns=[b'personal:hero', b'professional:name', b'custom:color'])
print('hero: {}, name: {}, color: {}'.format(
    row[b'personal:hero'], row[b'professional:name'], row[b'custom:color'])
)

connection.close()
