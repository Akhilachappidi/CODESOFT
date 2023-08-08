import random
import string

def create_password(length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choice(char_set) for _ in range(length))
    return new_password

def generate_user_password():
    print("Welcome to the Password Generator!")
    
    try:
        pwd_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")
        return

    if pwd_length <= 0:
        print("Invalid input! Password length should be a positive integer.")
        return

    password = create_password(pwd_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    generate_user_password()
