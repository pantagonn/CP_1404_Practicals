"""
CP1404/CP5632 Practical
Pantagon Intajuck
Word occurrence counter
"""

words_to_count = {}
sentence = input("Please enter a sentence: ")
list_of_words = sentence.split()
list_of_words.sort()

for word in list_of_words:
    word_counter = words_to_count.get(word, 0)
    words_to_count[word] = word_counter + 1

maximum_word_length = max((len(word) for word in list_of_words))

for word, word_count in words_to_count.items():
    print(f"{word:{maximum_word_length}} : {word_count}")
