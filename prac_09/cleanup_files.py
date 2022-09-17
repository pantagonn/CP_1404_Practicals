"""
Clean up files
"""
import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            original_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(original_name, new_name)
            print(f"Successfully changed {original_name} to {new_name}")


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_title = ""
    original_title = (filename.replace(".TXT", ".txt").replace(".txt", ""))
    for index, character in enumerate(original_title):
        if character.isalpha():
            try:
                previous_character = original_title[index - 1]
                next_character = original_title[index + 1]
                if next_character.isupper():
                    character += "_"
                elif previous_character == "_":
                    character = character.upper()
            except IndexError:
                pass
        elif character.isspace():
            character = "_"
        new_title += character
    new_title += ".txt"
    return new_title


main()
