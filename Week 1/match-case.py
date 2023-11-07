def main():
    length = int(input('How long is the word? '))
    valid_words = load_words('1-1000.txt', length)
    print('Words Loaded!')
    guess = input('What is the word? ')
    print(check_valid(valid_words, guess))
    return

def load_words(filename, l):
    """
    Read the contents of the given file.  Assumes the file contents contain
    different words in each line.

    Parameters:
    filename - the name of the data file as a string
    length - the length of the word

    Returns:
    a list of words of length l
    """

    words = []

    with open(filename, 'r') as f:
        for word in f:
            stripped_word = word.strip()  # Strip whitespace and newline characters
            if len(stripped_word) == l:  # Check if the length matches after stripping
                words.append(stripped_word)  # Append the stripped word
    return words

def check_valid(words, guess):
    for word in words:
        match word:
            case guess:
                return 'Valid'
    return 'Invalid'

main()