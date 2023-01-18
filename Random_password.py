import random
import string

def generate_password(length: int):
    """
    Generates a random password of the specified length
    """
    # create a list of all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password
    password = "".join(random.choice(characters) for i in range(length))

    return password

print(generate_password(12))
