import sqlite3

# Create database Connection
con = sqlite3.connect('user.db')

#
# to execute queries and fetch data we have to use cursor

cur = con.cursor()

listOfTables = cur.execute(
  """SELECT tableName FROM sqlite_master WHERE type='table'; """).fetchall()

print("ListOfTable::",listOfTables)

# Create a Table for User

cur.execute("""CREATE TABLE user (
    full_name text,
    street_name text,
    house_no text,
    zip_code text,
    city text,
    email text,
    mobile_phone text
)""")
            
# Create a Table for logs
            
# Datatypes
# Null
# Integer
# REAL
# TEXT
# BLOB

# Commit our command
con.commit()

# Close the connection

con.close()

# find user by Id







