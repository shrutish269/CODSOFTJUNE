# task3.py
import random

# Define character sets
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

all_characters = lowercase + uppercase + numbers + symbols

print("Password Generator")

try:
    length = int(input("Enter the desired password length: "))

    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        password = ""
        for i in range(length):
            password += random.choice(all_characters)

        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
