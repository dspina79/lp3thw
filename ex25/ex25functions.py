
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words in alphabetical order"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off the array """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word in the array after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence): 
    """Takes in a full sentence and reorders the words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words in a sentence"""
    words = break_words(sentence)
    print_first_and_last_words(words)

def print_first_and_last_words(words):
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_and_last_words(words)