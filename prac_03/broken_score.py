"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter your score: "))
while 0 < score <= 100:
    if score >= 90:
        print("Excellent score!")
    elif score >= 50:
        print("Passable score!")
    else:
        print("Bad score!")
    score = float(input("Enter your score: "))
print("Invalid score!")



