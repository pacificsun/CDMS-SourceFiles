
import sqlite3
import datetime
import zipfile
import re

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
  
    print("TABLES CREATED SUCCESSFULLY!!!")
   


# Commit our command
con.commit()

# Close the connection

con.close()

# regex  input validation functions

# function validating an Email
def email_validation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return email
    else:
        print("Invalid Email")
        return email
    
# function validating phonenumber
def phonenumber_validation(phonenumber):
    validated_phonenumber = phonenumber.strip()
    phonenumber_with_code = '+1-6-'+validated_phonenumber
    return phonenumber_with_code

#Caesar cipher encryption       
def encrypt_password(plaintext, n):
    ans=""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans+=" "
        elif(ch.isupper()):
            ans+= chr((ord(ch) + n-65) % 26 + 65)

        else:
            ans+= chr(ord(ch) + n-97 % 26 + 97)
    return ans

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
    
    valid_email = email_validation(email)
    valid_phonenumber = phonenumber_validation(mobile_phone)

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
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (username, fname, lname, street_name, house_no, zip_code, city, valid_email, valid_phonenumber, role, password, date))
    except:
        raise Exception("Error Occured")
    finally:
        db.commit()
        db.close()

# Advisor's functions

def add_advisor():
    username = input("Enter Advisor's username: ")
    fname = input("Enter Advisor's first name: ")
    lname = input("Enter Advisor's last name: ")
    street_name = input("Enter Advisor's street name: ")
    house_no = input("Enter Advisor's house no: ")
    zip_code= input("Enter Advisor's zip code: ")
    city = input("Enter Advisor's city: ")
    email = input("Enter Advisor's email: ")
    mobile_phone = input("Enter Advisor's mobile phone: ")
    role = 'Advisor'
    password = input("Enter Advisor's password: ")
    date = datetime.datetime.now()

    encrypted_password = encrypt_password(password, 1)
    insert_user_record(username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, encrypted_password, date)      


def update_advisor_password():
    username = input("Enter advisor's username that you want to update: ")
    user_check = get_user_by_username(username)
    if user_check:
        newpassword = input("Enter new password: ")
        try: 
            db = sqlite3.connect('user.db')
            cursor = db.cursor()
            sql_statement = "UPDATE users set password=? WHERE username=?"
            data = cursor.execute(sql_statement, (newpassword,username))
            db.commit()
        except:
            raise Exception("Error occured")
        finally:
            db.close()

def get_all_advisor():
    role="Advisor"
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE role=?"
        data = cursor.execute(sql_select_query,(role,))


        for record in data:
            # print("Record",record)
            print("USERNAME: ", record[0])
            print ("ROLE: ", record[9]+'\n')
           
    finally:
        db.close()

 # Admin's functions        

def add_admin():
    username = input("Enter Admin's username: ")
    fname = input("Enter Admin's first name: ")
    lname = input("Enter Admin's last name: ")
    street_name = input("Enter Admin's street name: ")
    house_no = input("Enter Admin's house no: ")
    zip_code= input("Enter Admin's zip code: ")
    city = input("Enter Admin's city: ")
    email = input("Enter Admin's email: ")
    mobile_phone = input("Enter Admin's mobile phone: ")
    role = 'Admin'
    password = input("Enter Admin's password: ")
    date = datetime.datetime.now()

    encrypted_password = encrypt_password(password, 1)
    insert_user_record(username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, encrypted_password, date)

def get_user_by_username(username):
    # returns ture if username is found else returns false
    user_exist = True
    try: 
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE username=?"
        data = cursor.execute(sql_select_query,(username,))
        for row in data:
            print("row::", row)

        return user_exist
    except:
        raise Exception("Error occured")
    finally:
        db.close()

def get_all_user_and_role():
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        data = cursor.execute(''' SELECT * FROM users''')

        for record in data:
            # print("Record",record)
            print("USERNAME: ", record[0])
            print ("ROLE: ", record[9]+'\n')
           
    finally:
        db.commit()
        db.close()

def update_admin_password():
    username = input("Enter admin's username that you want to update: ")
    user_check = get_user_by_username(username)
    if user_check:
        new_password = input("Enter new password: ")
        newpassword = encrypt_password(new_password, 1)
        try: 
            db = sqlite3.connect('user.db')
            cursor = db.cursor()
            sql_statement = "UPDATE users set password=? WHERE username=?"
            data = cursor.execute(sql_statement, (newpassword,username))
            db.commit()
        except:
            raise Exception("Error occured")
        finally:
            db.close()

def delete_admin():
    username = input("Enter username that you want to delete: ")
    user_check = get_user_by_username(username)
    if user_check:
        try: 
            db = sqlite3.connect('user.db')
            cursor = db.cursor()
            sql_statement = "DELETE from users WHERE username=?"
            data = cursor.execute(sql_statement, (username,))
            db.commit()
        except:
            raise Exception("Error occured")
        finally:
            db.close() 

def get_all_admin():
    role="Admin"
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE role=?"
        data = cursor.execute(sql_select_query,(role,))


        for record in data:
            # print("Record",record)
            print("USERNAME: ", record[0])
            print ("ROLE: ", record[9]+'\n')
           
    finally:
        db.close() 

def check_auth(username, password):
    
    user_credential = {}
    encrypt_pass = encrypt_password(password, 1)

    #check the username password are correct
    try:
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE username=? AND password=?"
        data = cursor.execute(sql_select_query,(username,encrypt_pass))
        for row in data:
            user_credential["user_role"] = row[9]
            user_credential["Authenticate"] = True
            return user_credential
    except: 
        raise Exception('Error occured')
    finally:
        db.commit()
        db.close()


def get_user_information():
    username = input("Enter username: ").strip()
    try: 
        db = sqlite3.connect('user.db')
        cursor = db.cursor()
        sql_select_query = "SELECT * FROM users WHERE username=?"
        data = cursor.execute(sql_select_query,(username,))
        for row in data:
            print("USERNAME: ", row[0])
            print("FIRSTNAME: ", row[1])
            print("LASTNAME: ", row[2])
            print("STREET NAME: ", row[3])
            print("HOUSE NO: ", row[4])
            print("ZIP CODE: ", row[5])
            print("CITY: ", row[6])
            print("EMAIL: ", row[7])
            print("PHONE NUMBER: ", row[8])
            print("USER ROLE: ", row[9])
            print("PASSWORD: ", row[10])
            print("USER CREATED DATE: ", row[11])

        
    except:
        raise Exception("Error occured")
    finally:
        db.close()


def login_view():
    username = input("Enter username: ")
    password = input("Enter yourpassword: ")
    login_value = check_auth(username, password)
    if login_value == None:
        print("Wrong username or password!!!")
        super_main()    
    return login_value

# Create backup/zip file 
def create_backup():
    with zipfile.ZipFile('backup.zip', 'w') as z:
        z.write('user.db')


# This is main interface for the program
def super_main():
    login_value =  login_view()
    # print("login_value::", login_value)
    login_auth = login_value["Authenticate"]
    login_role = login_value["user_role"]
    if login_auth and login_role == "superadmin":
        def main():
            # get user Role

            # User menu
            print("                                     ")
            print("                                     ")
            print("                                     ")
            print("            ************************")
            print("             WELCOME SUPER ADMIN !!!")
            print("            ************************")
            print("""
            1. ADD ADMIN TO THE SYSTEM
            2. GET LIST OF USER AND ROLE
            3. UPDATE ADMIN'S PASSWORD
            4. DELETE ADMIN
            5. GET ALL ADMIN
            6. BACK UP
            7. SEARCH AND RETRIVE USER INFORMATION
            """)
            choice = input("ENTER YOUR CHOICE NUMBER OR ENTER 0 OR CMD/CTRL + C TO EXIT: ")
            system_exit = True
            while system_exit:
            
                if(choice == '0'):
                    print("Program Closed!!!")
                    system_exit = False
                    super_main()
                elif(choice == '1'):
                    add_admin()
                    print("A new admin added!!!")
                    main()
                elif(choice == "2"):
                    get_all_user_and_role()
                    main()
                elif(choice == "3"):
                    update_admin_password()
                    print("PASSWORD IS SUCCESFULLY UPDATED!!!")
                    main()
                elif(choice == "4"):
                    delete_admin()
                    print("ADMIN SUCCESFULLY DELETED!!!")
                    main()
                elif(choice == "5"):
                    get_all_admin()
                    main()
                elif(choice == "6"):
                    # Create Backup
                    create_backup()
                    print("BACKUP CREATED SUCCESFULLY!!!")
                    main()
                elif(choice == "7"):
                    get_user_information()
                    main()
                else:
                    print("wrong Choice!")
                    main()
                   
        main()
    
    elif login_auth and login_role == "Admin":
         def main():
            # get user Role

            # User menu
            print("                                     ")
            print("                                     ")
            print("                                     ")
            print("            ************************")
            print("                WELCOME ADMIN !!!")
            print("            ************************")
            print("""
            1. ADD ADVISOR TO THE SYSTEM
            2. GET LIST OF USER AND ROLE
            3. UPDATE ADVISOR'S PASSWORD
            4. DELETE ADVISOR
            5. GET ALL ADVISOR
            6. BACK UP
            7. SEARCH AND RETRIVE USER INFORMATION
            """)
            choice = input("ENTER YOUR CHOICE NUMBER OR ENTER 0 OR CMD/CTRL + C TO EXIT: ")
            system_exit = True
            while system_exit:
            
                if(choice == '0'):
                    print("Program Closed!!!")
                    system_exit = False
                    super_main()
                elif(choice == '1'):
                    add_advisor()
                    print("A new Advisor added!!!")
                    main()
                elif(choice == "2"):
                    get_all_user_and_role()
                    main()
                elif(choice == "3"):
                    update_advisor_password()
                    print("PASSWORD SUCCESFULLY UPDATED!!!")
                    main()
                elif(choice == "4"):
                    delete_admin()
                    print("ADVISOR SUCCESFULLY DELETED!!!")
                    main()
                elif(choice == "5"):
                    get_all_advisor()
                    main()
                elif(choice == "6"):
                    # Create Backup
                    create_backup()
                    print("BACKUP CREATED SUCCESFULLY!!!")
                    main()
                elif(choice == "7"):
                    get_user_information()
                    main()
                else:
                    print("wrong Choice!")
                    main()
                   
         main()
         
        
        
        


# To run the supermain function.

super_main()
