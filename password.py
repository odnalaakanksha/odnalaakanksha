import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    character_set = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password using random.choice() function
    password = ''.join(random.choice(character_set) for _ in range(length))

    return password

def main():
    print("Welcome to Password Generator!")
    length = int(input("Enter desired length of the password (min. 4, max. 16): "))

    # Ensure the length is within the allowed range
    if length < 4 or length > 16:
        print("Invalid length. Please enter a value between 4 and 16.")
        return

    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
