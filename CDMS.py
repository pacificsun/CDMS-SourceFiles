
import sqlite3
import datetime

# Create database Connection
con = sqlite3.connect('user.db')

#
# to execute queries and fetch data we have to use cursor

cur = con.cursor()

listOfTables = cur.execute("""SELECT * FROM sqlite_master WHERE type='table'
  AND name='users'; """).fetchall()


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


# Commit our command
con.commit()

# Close the connection

con.close()

# regex function

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

def add_admin():
    username = input("Enter Admin's username: ")
    fname = input("Enter Admin's first name: ")
    lname = input("Enter Admin's last name: ")
    street_name = input("Enter Admin's street name: ")
    house_no = input("Enter Admin's house no: ")
    zip_code= input("Enter Admin's zip code: ")
    city = input("Enter Admin's city: "),
    email = input("Enter Admin's email: ")
    mobile_phone = input("Enter Admin's mobile phone: ")
    role = 'Admin'
    password = input("Enter Admin's password: ")
    date = datetime.datetime.now()
    # TODO: encrypt the password
    insert_user_record(username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, password, date)

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
    
    user_credential = {}
    
    #check the username password are correct
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE username=? AND password=?"
        data = cursor.execute(sql_select_query,(username,password))
        for row in data:
            user_credential["user_role"] = row[10]
            user_credential["Authenticate"] = True
            print(user_credential)
            return user_credential
    except: 
        raise Exception('Error occured')
    finally:
        db.commit()
        db.close()



def login_view():
    username = input("Enter username: ")
    password = input("Enter yourpassword: ")
    login_value = check_auth(username, password)
    print("login_value::", login_value)
    if login_value == None:
        print("Wrong username or password!!!")
        super_main()    
    return login_value['Authenticate']


# This is main interface for the program
def super_main():
    if login_view():
        def main():
            # get user Role

            # User menu
            print("Welcome!!!")
            print("*************")
            print("""
            1. ADD ADMIN TO THE SYSTEM
            2. UPDATE ADMIN'S PASSWORD
            3. UPDATE ADMIN'S DETAILS
            4. DELETE ADMIN
            5. GET ALL ADMIN
            6. BACK UP
            """)
            choice = input("ENTER YOUR CHOICE NUMBER OR ENTER 0 TO EXIT : ")
            print("choice>>", choice)
            system_exit = True
            while system_exit:
            
                if(choice == '0'):
                    print("Program Closed")
                    system_exit = False
                elif(choice == '1'):
                    add_admin()
                    print("A new admin added!!!")
                elif(choice == "2"):
                    get_user()
                else:
                    print("wrong Choice")
                    main()
        main()
        


def create_user():
    print("User create function")
def get_user():
    print("get a user")
def update_user():
    print("Update user")
def update_user():
    print("update user")


# To run the supermain function.

super_main()
