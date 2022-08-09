"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Display all subject details"""
    data = get_data()
    print("Data >>>>", data)
    show_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def show_subjects(data):
    """Display each subject detail"""
    for subject_data in data:
        subject_code = subject_data[0]
        name_of_lecturer = subject_data[1]
        number_of_students = subject_data[2]
        print(f"{subject_code} is taught by {name_of_lecturer:14} and has {number_of_students:4} students")


main()
