import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default is y): ").lower() != 'n'
    use_special_chars = input("Include special characters? (y/n, default is y): ").lower() != 'n'
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()