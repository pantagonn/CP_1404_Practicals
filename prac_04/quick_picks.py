"""
Quick Picks
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Generate 6 random numbers for each line that user specified """
    number_of_lines = int(input("How many quick picks? "))
    while 0 > number_of_lines:
        print("Error: There must be at least ONE quick pick.")
        number_of_lines = int(input("How many quick picks? "))
    for j in range(number_of_lines):
        quick_pick = []
        for k in range(6):  # there are six numbers each line
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        # print(f"{number:2}" for number in quick_pick) had to look at solution sorry :(
        print(" ".join("{:2}".format(number) for number in quick_pick))





main()
