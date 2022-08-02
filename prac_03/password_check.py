"""
Password Check Program
"""


def main():
    """Print password."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get password from users."""
    user_input = str(input("What is your password?: "))
    return user_input


def print_stars(length):
    """Print the length of password in asterisks."""
    print(len(length) * "*")


main()
