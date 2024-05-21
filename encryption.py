from cryptography.fernet import Fernet
#will take a input as string and complete it into a complete random character!!


def encrypt_password(password):
    
    pass
pwd=input("enter a password!!")
def write_key():
    key= Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)