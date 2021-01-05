import ex25functions as ex25

# start with the sentence
sentence = "All good things come to those who wait"

# break it up and display
words = ex25.break_words(sentence)
print(words)

# sort the words and display
sorted_words = ex25.sort_words(words)
print(sorted_words)

# print the first and the last of the unsorted words
ex25.print_first_word(words)
ex25.print_last_word(words)
print(words)

# print the first and the last of the sorted words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print(sorted_words)

# use print first and last for the whole sentence
# sorted and unsorted
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
