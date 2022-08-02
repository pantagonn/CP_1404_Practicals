"""
Broken program to determine score status.
"""

import random

def main():
    """Get score from user and print the result."""
    score = float(input("Enter your score: "))
    print(evaluate_score(score))
    random_grade = (random.randint(0, 100))  # generate random grade
    print("Random grade: {}".format(random_grade))
    print(evaluate_score(random_grade))


def evaluate_score(score):
    """Evaluate user's score."""
    while 0 < score <= 100:
        if score >= 90:
            return "Excellent score!"
        elif score >= 50:
            return "Passable score!"
        else:
            return "Bad score!"
    return "Invalid score!"


main()
