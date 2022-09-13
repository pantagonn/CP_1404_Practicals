"""
Taxi simulator
"""

from prac_08.silver_service_taxi.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi.taxi import Taxi

list_of_taxis = [Taxi("Limo", 150), SilverServiceTaxi("Royce Phantom", 400, 2), SilverServiceTaxi("Hummer", 320, 5)]


def main():
    current_taxi = None
    bill_in_total = 0
    distance_in_total = 0
    user_input = main_menu()
    while user_input != "q":
        if user_input == "c":
            current_taxi = choose_taxi()
        else:
            bill_in_total += drive(current_taxi)
        display_bill(bill_in_total)
        user_input = main_menu()
    print("--------------------")
    display_bill(bill_in_total)
    print(f"You have travelled {total_distance_tracker(distance_in_total)} km in total.")
    display_taxis()
    quit()


def display_menu():
    """List down menu choices and prompt"""
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")


def main_menu():
    """Display menu to get user's input"""
    display_menu()
    user_choice = get_valid_input()
    return user_choice


def get_valid_input():
    """Ensure the validity of user's input"""
    choice = input('>>>').lower()
    while choice not in ["q", "c", "d"]:
        print('Invalid Option')
        display_menu()
        choice = input('>>>').lower()
    return choice


def display_bill(bill):
    """Display the total trip cost"""
    print(f"Bill in total :${bill}")


def display_taxis():
    """Display all available taxis."""
    print("Taxis available:")
    for index, taxi in enumerate(list_of_taxis):
        print("{} - {}".format(index, taxi))


def choose_taxi():
    """Display a list of taxis for selection"""
    display_taxis()
    try:
        taxi_choice = int(input("Please choose a taxi: "))
        if taxi_choice < 0 or taxi_choice > len(list_of_taxis) - 1:
            print("Invalid Taxi Choice")
            return None
        print(f"{list_of_taxis[taxi_choice].name} has been chosen.")
        return list_of_taxis[taxi_choice]
    except ValueError:
        print("Error: Invalid choice")
        return None


def total_distance_tracker(total_distance):
    """Keep track of the total traveling distance"""
    for taxi in list_of_taxis:
        total_distance += taxi.odometer
    return total_distance


def drive(current_taxi):
    """Drive the taxi according to user's distance input"""
    if current_taxi is None:
        print("Error: No taxi available for driving")
        return 0
    else:
        try:
            traveling_distance = int(input("Please indicate driving distance: "))
            if traveling_distance < 0:
                print("Error: Driving distance cannot be less than zero miles")
                return 0.0
            current_taxi.drive(traveling_distance)
            fare = current_taxi.get_fare()
            print(f"Your trip in {current_taxi.name} will cost you ${fare}")
            current_taxi.start_fare()
            return fare
        except ValueError:
            print("Error: Invalid Input")
            return 0.0


main()
