
import sqlite3

# Create database Connection
con = sqlite3.connect('user.db')

#
# to execute queries and fetch data we have to use cursor

cur = con.cursor()

listOfTables = cur.execute("""SELECT * FROM sqlite_master WHERE type='table'
  AND name='users'; """).fetchall()

print("ListOfTable::", listOfTables)

if(listOfTables) == []:
        # Create a Table for User
    cur.execute("""CREATE TABLE users (
            username text,
            fname text,
            lname text,
            street_name text,
            house_no text,
            zip_code text,
            city text,
            email text,
            mobile_phone text,
            role text,
            password text,
            date text
    )""")
    cur.execute(''' INSERT INTO users(
            username,
            fname,
            lname,
            street_name,
            house_no,
            zip_code,
            city,
            email,
            mobile_phone,
            role,
            password,
            date
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', ('superadmin','Admin', 'Admin', 'Wolf Street',"4000A",'76904','San Angelo','superadmin@gmail.com','+1-6-32562529','superadmin','Admin!23', '15-03-2023' ))
            
# Create a Table for logs

    # cur.execute("""CREATE TABLE logs (
    #     username text,
    #     date text,
    #     Time text,
    #     description_of_activity text,
    #     additional_information text,
    #     suspicious text
    # )""")
    print("TABLES CREATED SUCCESSFULLY!!!")
    print("SYSTEM DATA IS LOADED SUCCESSFULLY!!!")


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

# functions
def  insert_user_record(username,
        fname,
        lname,
        street_name,
        house_no,
        zip_code,
        city,
        email,
        mobile_phone,
        role,
        password,
        date
        ):
    print(username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, password, date)
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        cursor.execute(''' INSERT INTO users(
            username,
            fname,
            lname,
            street_name,
            house_no,
            zip_code,
            city,
            email,
            mobile_phone,
            role,
            password,
            date
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, password, date))
    finally:
        db.commit()
        db.close()

def get_all_user():
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        data = cursor.execute(''' SELECT * FROM users ORDER BY username''')
        for record in data:
            #print 'ID : '+str(record[0])
            # print 'NAME : '+str(record[1])
            # print 'DIVISION : '+str(record[2])
            # print 'STARS : '+str(record[3])+'\n'
            print("record::", record)
    finally:
        db.commit()
        db.close()

def check_auth(username, password):
    print(username, password)
    #check the username password are correct
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE username=? AND password=?"
        data = cursor.execute(sql_select_query,(username,password))
        print("data>>", data)
        for row in data:
           
            print(row)
            return row[11]
    except: 
        raise Exception('Error occured')
    finally:
        db.commit()
        db.close()



def login_view():
    username = input("Enter username: ")
    password = input("Enter yourpassword: ")
    check_auth(username, password)


# This is main interface for the program
if login_view():
    def main():
       
        # User menu
        print("Welcome!!!")
        print("*************")
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
                get_all_user()

                
            elif(choice == "2"):
                get_user()
            else:
                print("wrong Choice")
                main()
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



