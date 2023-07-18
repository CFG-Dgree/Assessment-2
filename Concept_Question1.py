class OverOneWord(Exception):
    pass

def is_isogram(word):

    word = word.lower()
    unique_letters = set()

    # should not over one word
    if len(word.split()) > 1:
        raise OverOneWord("Input should contain only one word")
    # Iterate through each letter in the word
    for letter in word:
        #  check repeated letter
        if letter in unique_letters:
            return False

        unique_letters.add(letter)

    # If no repeated letters were found, it's an isogram
    return True
