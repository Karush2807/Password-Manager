from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from encryption import encrypt_password, decrypt_password

client=MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/") #this will link python to our mongodb database
data_base=client["PasswordManager"] #ye jo hmara database hai, uska name hai
pass_collections=data_base['PassStorage'] #ye jo hmne uske andar colllection bnayi hai, vo hai ye

#function to add password
def add_password(platform, username, password):
    encrypted_password=encrypt_password(password)
    pass_collections.insert_one({'Platform Name': platform,
                                "UserName": username,
                                "Password": Binary(encrypted_password)})
    print("data added succesfully :)")

#function to update the existinng password!!
def update_password(id, password):
    encrypted_password=encrypt_password(password)
    pass_collections.update_one(
        {'_id': ObjectId(id)},
        {"$set": {'Password': encrypted_password}}
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
        decrypted_password = decrypt_password(wordpass['Password'])

        print(
            f"ID: {wordpass['_id']},"
            f"PLatform Name {wordpass['Platform Name']},"
            f"User Name {wordpass['UserName']},"
            f"Password {decrypted_password}"
            
        )