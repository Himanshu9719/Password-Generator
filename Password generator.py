import random
import string

# Welcome message
print("🔐 Password Generator")

# Ask user for password length
length = int(input("Enter password length (e.g., 8, 12, 16): "))

# Ask what to include in the password
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include special characters? (y/n): ").lower() == 'y'

# Build character set
characters = ""
if include_letters:
    characters += string.ascii_letters  # a-z + A-Z
if include_digits:
    characters += string.digits         # 0-9
if include_symbols:
    characters += string.punctuation    # !@#$%^&* etc.

# Ensure at least one character set is selected
if not characters:
    print("⚠️ You must select at least one type of character!")
else:
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\n🔑 Your secure password is:", password)
