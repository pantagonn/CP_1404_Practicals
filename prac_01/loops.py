"""
Loops exercises
"""

# example:

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100:

for j in range(0, 101, 10):
    print(j, end=' ')
print()

# b. count down from 20 to 1:

for j in range(20, 0, -1):
    print(j, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line:

number_of_stars = int(input("How many stars? : "))
for j in range(number_of_stars):
    print('*', end=' ')
print()

# d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1.

number_of_stars = int(input("How many stars? : "))
for j in range(1, number_of_stars + 1):
    print("*" * j)
print()
