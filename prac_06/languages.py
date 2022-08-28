"""
Client code for programming languages
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """ List down details of different programming languages"""
    list_of_programs = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    list_of_programs.append(ruby)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    list_of_programs.append(python)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    list_of_programs.append(visual_basic)

    for language in list_of_programs:
        print(language)
    print("The dynamically typed languages are:")
    for language in list_of_programs:
        if language.is_dynamic():
            print(language.field)


main()
