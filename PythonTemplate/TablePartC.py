import happybase as hb
import csv

# Connect to the database
connection = hb.Connection('localhost')
connection.open()

# Insert data from input.csv file into the 'powers' table
with open('input.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        connection.table('powers').put(
            row[0],
            {
                'personal:hero': row[1],
                'personal:power': row[2],
                'professional:name': row[3],
                'professional:xp': row[4],
                'custom:color': row[5]
            }
        )

# Close the connection
connection.close()
