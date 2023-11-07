def main():
    length = input('How long is the word? ')
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

    list = []

    f = open(filename, 'r')

    for word in f:
        if len(word) == l:
            list.append(word)
    return list

def check_valid(words, guess):
    for word in words:
        match word:
            case guess:
                return 'Valid'
    return 'Invalid'

main()