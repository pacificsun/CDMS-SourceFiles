
import sqlite3

# Create database Connection
con = sqlite3.connect('user.db')

#
# to execute queries and fetch data we have to use cursor

cur = con.cursor()

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

cur.execute("""CREATE TABLE logs (
    username text,
    date text,
    Time text,
    description_of_activity text,
    additional_information text,
    suspicious text
)""")
         
            
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


# This is main interface for the program
def main():
    print("""
    1. ADD CLIENT TO THE SYSTEM
    2. UPDATE PASSWORD
    3. UPDATE CLIENT
    4. SEARCH AND RETRIVE CLIENT
    5. GET ALL CLIENTS
    """)
    choice = input("ENTER YOUR CHOICE NO OR ENTER 0 TO EXIT : ")
    print("choice>>", choice)
    system_exit = True
    while system_exit:
        if(choice == '0'):
            print("Program Closed")
            system_exit = False
        elif(choice == '1'):
            create_user()
            
        elif(choice == "2"):
            get_user()
        else:
            print("wrong Choice")
            main()
        


def create_user():
    print("User create function")
    main()
def get_user():
    print("get a user")
def update_user():
    print("Update user")
def update_user():
    print("update user")
def loginView():
    
    name = input("Enter your username: ")
    password = input("Enter your password: ")
     
     # check user in database

main()