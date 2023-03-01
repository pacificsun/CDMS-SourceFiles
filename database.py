import sqlite3

# Create database Connection
con = sqlite3.connect('user.db')

# to execute queries and fetch data we have to use cursor

cur = con.cursor()
