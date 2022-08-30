"""
Client code for guitar program
"""

from prac_06.guitar import Guitar

list_of_guitars = []


def main():
    get_guitar_input()
    display_guitars()


def get_guitar_input():
    """Get user's input for guitar"""
    name = input("Enter guitar's name: ")
    while name != "":
        year = int(input("Enter guitar's year: "))
        cost = float(input("Enter guitar's cost: "))
        list_of_guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar's name: ")


def display_guitars():
    """Display all guitars' information including the vintage status"""
    if not list_of_guitars:
        print("I currently do not have any guitars :(")
    else:
        print("These are my guitars: ")
        for index, guitar in enumerate(list_of_guitars, 1):
            if guitar.is_vintage():
                print(f"Guitar {index}: {guitar.name.title()} ({guitar.year}), worth ${guitar.cost:.2f} (vintage)")
            else:
                print(f"Guitar {index}: {guitar.name.title()} ({guitar.year}), worth ${guitar.cost:.2f}")


main()
