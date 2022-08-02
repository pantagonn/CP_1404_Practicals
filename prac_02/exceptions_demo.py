"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Q1: When will a ValueError occur?
# A: When user does not enter either a valid numerator or denominator number (eg. a, b, etc).

# Q2: When will a ZeroDivisionError occur?
# A: When user enters number zero as denominator.

# Q3: Could you change the code to avoid the possibility of a ZeroDivisionError?
# A: To my current knowledge, I could possibly try to avoid it by using an if statement.
# (Although, i am not sure if it is the right approach)

""" Old Code """
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

""" New Code """
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator != 0:
        fraction = numerator / denominator
    else:
        fraction = "Cannot divide by zero!"
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")



