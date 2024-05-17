from pymongo import MongoClient
from bson import ObjectId
import pyqrcode
import png

client=MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/") #this will link python to our mongodb database

data_base=client["PasswordManager"] #ye jo hmara database hai, uska name hai
pass_collections=data_base['PassStorage'] #ye jo hmne uske andar colllection bnayi hai, vo hai ye

#function to add password
def add_password(platform, username, password):
    pass

def update_password(id, platform, username, password):
    pass

def delete_password(id):
    pass

def show_passwords():
    pass

def generate_password(platform, username):
    pass

def create_qr(platform, username, password):
    pass

def encrypt_password(password):
    pass


def main():
    print("Welcome to this Password Manager APP!!")
    print("1. Add a new password")
    print("2. Update a password")
    print("3. Delete a password")
    print("4. Show all passwords")
    print("5. Generate a password")
    print("6. Create a QR code")
    print("7. Encrypt a password")
    print("8. Exit")
    
    user_choice=input("Enter your choice[1-8]: ")

    if user_choice==1:
        add_password()

    elif user_choice==2:
        update_password()

    elif user_choice==3:
        delete_password()

    elif user_choice==4:
        show_passwords()

    elif user_choice==5:
        generate_password()

    elif user_choice==6:
        create_qr()

    elif user_choice==7:
        encrypt_password()

    else:
        print("Invalid choice! Please try again!")
    






if __name__ =="__main__":
    main()
