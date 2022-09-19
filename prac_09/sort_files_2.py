"""
Sort files according to their file type
"""

import os
import shutil


def main():
    """Sort files according to their type and move them to folders"""
    os.chdir("FilesToSort")
    file_extensions = {}
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        split_file = filename.split(".")
        # print(split_file)
        if len(split_file) == 2:
            file_extension = split_file[1]
            if file_extension in file_extensions:
                file_extensions[file_extension].append(filename)
            else:
                file_extensions[file_extension] = [filename]
    # Version 2
    file_types = {}
    for file_extension in file_extensions.keys():
        file_type = input(f"What category would you like to sort {file_extension} files into? ")
        if file_type in file_types:
            file_types[file_type] += file_extensions[file_extension]
        else:
            file_types[file_type] = file_extensions[file_extension]

    for file_type, files in file_types.items():
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        for filename in files:
            shutil.move(filename, f"{file_type}/" + filename)


main()