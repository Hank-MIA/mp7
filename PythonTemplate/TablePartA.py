import happybase as hb

connection = hb.Connection('localhost')
connection.open()

# Create a table named "powers" with three column families named personal, professional and custom, all strings
connection.create_table('powers', {'personal': dict(), 'professional': dict(), 'custom': dict()})
# Create a table named "food" with two column families named nutrition and taste, all strings
connection.create_table('food', {'nutrition': dict(), 'taste': dict()})

# Close the connection
connection.close()
