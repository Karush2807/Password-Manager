from cryptography.fernet import Fernet
#will take a input as string and complete it into a complete random character!!

#one-time run hoga, bs key generate krne ke liye
# def write_key():
#     key= Fernet.generate_key()#thisk key must be safe, as anyone with  key can decrypt data
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key() #this will generate a key file in the same directory as this file

def load_key():
    return open("key.key", "rb").read()

key = load_key()
cipher_suite = Fernet(key)

def encrypt_password(password):
    encrypted_pass=cipher_suite.encrypt(password.encode())
    return encrypted_pass

def decrypt_password(encrypt_pass):
    decrypted_password = cipher_suite.decrypt(encrypt_pass.decode())
    return decrypted_password.decode()
