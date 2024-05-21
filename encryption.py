from cryptography.fernet import Fernet
#will take a input as string and complete it into a complete random character!!

key= Fernet.generate_key() #thisk key must be safe, as anyone with  key can decrypt data
cipher_suite= Fernet(key)

def encrypt_password(password):
    encrypted_pass=cipher_suite.encrypt(password.encode())
    return encrypted_pass

def decrypt_password(encrypt_pass):
    decrypted_password = cipher_suite.decrypt(encrypt_pass).decode()
    return decrypted_password
