"""
CP1404/CP5632 Practical
Pantagon Intajuck
Email name storage program
"""


def main():
    """Store name from user email and print"""
    email_to_name = {}
    user_email = input("Please enter your email: ")
    while user_email != "":
        user_email = check_user_name(email_to_name, user_email)
    maximum_name_length = max((len(word) for word in email_to_name))
    for name, email in email_to_name.items():
        print(f"{name:{maximum_name_length}}: {email}")
    print("Thank You :)")


def check_user_name(email_to_name, user_email):
    """Check whether the name stated on the email is the user's actual name and add to dictionary"""
    user_name = extract_email_name(user_email)
    check = input(f"Is your name {user_name}? (Y/n): ").lower()
    while check != 'y' and check != 'n':
        print('Error: Invalid Input')
        check = input(f"Is your name {user_name}? (Y/n): ").lower()
    if check == 'y':
        email_to_name[user_name] = user_email
    else:
        user_name = input('Enter Name :')
        email_to_name[user_name] = user_email
    user_email = input("Please enter your email: ")
    return user_email


def extract_email_name(user_email):
    """Extract the user's name from the given email"""
    prefix = user_email.split('@')[0]
    parts = prefix.split('.')
    user_name = " ".join(parts).title()
    return user_name


main()
