"""
CP1404/CP5632 Practical
Pantagon Intajuck
Hexadecimal code producer
"""

NAME_TO_CODE = {"battleshipgray": "#848482", "babypink": "#f4c2c2", "beige": "#f5f5dc", "coral": "#ff7f50",
                "mandarin": "#f37a48", "rust": "#b7410e", "skobeloff": "#007474", "taupe": "#8b8589",
                "vanillaice": "#f38fa9", "xanadu": "#738678"}

color_choice = input("Please enter your desired color's name: ").lower()
while color_choice != "":
    if color_choice in NAME_TO_CODE:
        print(f"{color_choice.title()}'s hexadecimal code is {NAME_TO_CODE[color_choice]}")
    else:
        print("Invalid color choice!")
    color_choice = input("Please enter your desired color's name: ").lower()
