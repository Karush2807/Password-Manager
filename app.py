from pymongo import MongoClient #to connect mongoDB and vscode
from bson import ObjectId 
import pyqrcode #for creating qr code for the given user and password
import png #for save the created qr image
import random
import string

client=MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/") #this will link python to our mongodb database

data_base=client["PasswordManager"] #ye jo hmara database hai, uska name hai
pass_collections=data_base['PassStorage'] #ye jo hmne uske andar colllection bnayi hai, vo hai ye

#function to add password
def add_password(platform, username, password):
    pass_collections.insert_one({'Platform Name': platform, "UserName": username, "Password": password})
    print("data added succesfully :)")

#function to update the existinng password!!
def update_password(id, password):
    pass_collections.update_one(
        {'_id': ObjectId(id)},
        {"$set": {'Password': password}}
    )
    print("Passwords updated succesfully :)")

#function to delete password!!
def delete_password(id):
    pass_collections.delete_one(
        {'_id': ObjectId(id)},
    )
    print("Data deleted succesfully :)")

#function to show list of all passwords
def show_passwords():
    for wordpass in pass_collections.find():
        print(
            f"ID: {wordpass['_id']},"
            f"PLatform Name {wordpass['Platform Name']},"
            f"Password {wordpass['Password']}"
        )


def generate_password(platform, username, length):
    if length<5:
        raise ValueError("password length, should not be less than 5 characters!!")
    
    #defing all the datasets, we are using for creating password!!
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special=string.digits
    punctuations=string.punctuation

    #ensuring selection from all the datasets!!
    password=[
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
        random.choice(punctuations),
    ]

    all_char= upper+lower+digits+special+punctuations
    password+=random.choices(all_char, k=length-5)

    #shuffling the password for more randomness!!
    random.shuffle(password)

    #convert list to string and strng
    generated_pass= ''.join(password)
    return generated_pass
    


    

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
    
    user_choice=int(input("Enter your choice[1-8]: "))

    if user_choice==1:
        social_name=input("enter name of Social Platform: ")
        user_name=input("enter your username: ")
        passward=input("enter password: ")
        add_password(social_name, user_name, passward)

    elif user_choice==2:
        id=input("enter the id associated with the credentials: ")
        
        if pass_collections.find_one({'_id': ObjectId(id)}) :
            new_password=input("enter the new password: ")
            confirm_new_password=input("eneter the new password: ")

            if (new_password!= confirm_new_password):
                print("both passwords should match!!")
            
            else:
                update_password(id, confirm_new_password)

        else:
            print("entered id is invalid!!")

    elif user_choice==3:
        id=input("enter the id for the credentials to be deleted")
        
        if pass_collections.find_one({'_id': ObjectId(id)}):
            delete_password(id)

        else:
            print("Invalid Id")

    elif user_choice==4:
        show_passwords()

    elif user_choice==5:
        plat_name=input("enter which platform credentials you want to generate password!!")
        userNAME=input("enter username for which you want to generate: ")
        length=int(input("enter the length of password: "))
        print(generate_password(plat_name, userNAME, 14))

    elif user_choice==6:
        create_qr()

    elif user_choice==7:
        encrypt_password()

    else:
        print("Invalid choice! Please try again!")
    






if __name__ =="__main__":
    main()
