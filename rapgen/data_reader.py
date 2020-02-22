import string


def read_data(input_file):
    """
    Reads the text in the input file, strips punctuation, and splits it into words.

    :param input_file: A text based file to read from.
    :return: A list of words.
    """

    with open(input_file, 'r') as in_file:
        data = in_file.read().split()
    return [word.translate(str.maketrans('', '', string.punctuation)) for word in data]
