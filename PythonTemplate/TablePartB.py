import happybase as hb

# Connect to the database
connection = hb.Connection('localhost')
connection.open()

# List all the tables in the database
print(connection.tables())

# Close the connection
connection.close()
