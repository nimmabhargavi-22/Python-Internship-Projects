import random
import string


def generate_password(length):

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        else:
            has_special = True

    score = 0

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if len(password) >= 8:
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def save_password(password):

    with open("passwords.txt", "a") as file:
        file.write(password + "\n")


while True:

    print("\n===================================")
    print(" PASSWORD GENERATOR ")
    print("===================================")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        try:
            length = int(input("Enter Password Length: "))

            if length < 4:
                print("Password length should be at least 4")
                continue

            password = generate_password(length)

            print("\nGenerated Password:", password)

            strength = check_strength(password)

            print("Password Strength:", strength)

            save_password(password)

            print("Password Saved Successfully")

        except ValueError:
            print("Please Enter Numbers Only")

    elif choice == "2":

        password = input("Enter Password: ")

        strength = check_strength(password)

        print("Password Strength:", strength)

    elif choice == "3":

        print("Thank You")
        break

    else:

        print("Invalid Choice")