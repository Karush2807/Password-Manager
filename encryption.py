from cryptography.fernet import Fernet

# Function to write the key (run this once to generate the key)
# def write_key():
#     key = Fernet.generate_key()  # Generate a new encryption key
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)  # Save the key to a file

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()  # Read the key from the file

# Load the key from the file
key = load_key()
cipher_suite = Fernet(key)  # Initialize Fernet with the loaded key

# Function to encrypt a password
def encrypt_password(password):
    encrypted_pass = cipher_suite.encrypt(password.encode())  # Encrypt the password
    return encrypted_pass

# Function to decrypt an encrypted password
def decrypt_password(encrypt_pass):
    decrypted_password = cipher_suite.decrypt(encrypt_pass)  # Decrypt the password
    return decrypted_password.decode()  # Decode the decrypted password to string

