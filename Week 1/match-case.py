def load_words(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    different words in each line.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of length (int), words (list) pairs
    """

    dictionary = dict()

    f = open(filename, 'r')

    for word in f:
        length = len(word)
        if length in dictionary.keys():
            dictionary[length].append(word)
        else:
            dictionary[length] = [word]
    return dictionary