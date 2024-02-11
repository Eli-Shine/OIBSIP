import random
import string

print("Welcome to your random password generator program")

#Let's user enter their desired password length
length = int(input("Please enter desired password length: "))

# Ask the user for their preferences
use_lowercase = input("Do you want to include lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Do you want to include digits? (yes/no): ").lower() == 'yes'
use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'

# Create the character pool based on user preferences
characters = ''
if use_lowercase:
    characters += string.ascii_lowercase
if use_uppercase:
    characters += string.ascii_uppercase
if use_digits:
    characters += string.digits
if use_special_chars:
    characters += string.punctuation

# Check if at least one character type is selected
if not characters:
    print("Please select at least one character type.")
else:
    # Generate the password
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    print("Your generated password is:", password)
