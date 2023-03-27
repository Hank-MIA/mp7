import happybase as hb

connection = hb.Connection('localhost')
connection.open()

powers = connection.table('powers')

"""
nested for loop to achieve the same result as follows, as if HBase suported SQL:
SELECT p.name, p.power, p1.name, p1.power, p.color
FROM powers AS p
INNER JOIN powers AS p1
       ON p.color = p1.color
       AND p.name <> p1.name;
"""

for key, data in powers.scan():
    for key1, data1 in powers.scan():
        if data[b'custom:color'] == data1[b'custom:color'] and data[b'professional:name'] != data1[b'professional:name']:
            print('{}, {}, {}, {}, {}'.format(
                data[b'professional:name'], data[b'personal:power'],
                data1[b'professional:name'], data1[b'personal:power'], data[b'custom:color'])
            )

connection.close()

