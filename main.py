

def main():
    print("""
    1. ADD CLIENT TO THE SYSTEM
    2. UPDATE PASSWORD
    3. UPDATE CLIENT
    4. SEARCH AND RETRIVE CLIENT
    5. GET ALL CLIENTS
    """)
    choice = input("ENTER YOUR CHOICE NO : ")
    while True:
        if(choice == '1'):
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

    


