from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/") #this will link python to our mongodb database

data_base=client["PasswordManager"] #ye jo hmara database hai, uska name hai
pass_collections=data_base['PassStorage'] #ye jo hmne uske andar colllection bnayi hai, vo hai ye


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





if __name__ =="__main__":
    main()
