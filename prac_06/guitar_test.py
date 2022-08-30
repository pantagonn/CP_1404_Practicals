"""
Testing of guitar's functionality
"""

from prac_06.guitar import Guitar


guitar_number_one = Guitar('Gibson L-5 CES', 1922, 16035.40)
guitar_number_two = Guitar('Another Guitar', 2015, 10501.22)


def main():
    """Test the guitar"""
    print('{} get_age() - Expected 98. Got {}'.format(guitar_number_one.name, guitar_number_one.get_age()))
    print('{} get_age() - Expected 7. Got {}'.format(guitar_number_two.name, guitar_number_two.get_age()))
    print('{} is_vintage() - Expected True. Got {}'.format(guitar_number_one.name, guitar_number_one.is_vintage()))
    print('{} is_vintage() - Expected False. Got {}'.format(guitar_number_two.name, guitar_number_two.is_vintage()))


main()