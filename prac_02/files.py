"""
CP1404 - Practical
Files
"""

# Q1: Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# A:

out_file = open("files.txt", "w")
user_name = input("What is your name?: ")
print(f"Your name is {user_name}.", file=out_file)

out_file.close()

# Q2: Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
# A:

in_file = open("files.txt", "r")
name = in_file.read()
print(name)

in_file.close()

# Q3: Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the
# result, which should be... 59.
# A:

in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
print(first_number + second_number)

in_file.close()

# Q4: Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number
# of numbers.
# A:

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
print(total)

in_file.close()
