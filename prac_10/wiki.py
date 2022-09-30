"""
Wikipedia testing
"""

import wikipedia

user_input = input("Please enter something to search: ")

while user_input != "":
    try:
        page = wikipedia.page(user_input)
        print(f"Title: {page.title}")
        print(f"Url: {page.url}")
        print(f"Summary: {page.summary}")
        user_input = input("Please enter something to search: ")
    except wikipedia.DisambiguationError as e:
        print(e.options)
        user_input = input("Please enter something to search: ")