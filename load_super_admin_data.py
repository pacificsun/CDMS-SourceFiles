import sqlite3
import datetime
import re
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

def add_superadmin():
    username = input("Enter Super Admins's username: ")
    fname = input("Enter Super Admins's first name: ")
    lname = input("Enter Super Admins's last name: ")
    street_name = input("Enter Super Admins's street name: ")
    house_no = input("Enter Super Admins's house no: ")
    zip_code= input("Enter Super Admins's zip code: ")
    city = input("Enter Super Admins's city: ")
    email = input("Enter Super Admins's email: ")
    mobile_phone = input("Enter Super Admins's mobile phone: ")
    role = 'superadmin'
    password = input("Enter Super Admins's password: ")
    date = datetime.datetime.now()
    # TODO: encrypt the password
    encrypted_password = encrypt_password(password, 1)
    insert_user_record(username, fname, lname, street_name, house_no, zip_code, city, email, mobile_phone, role, encrypted_password, date)   

add_superadmin()