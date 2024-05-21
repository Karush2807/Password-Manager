import random
import string

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