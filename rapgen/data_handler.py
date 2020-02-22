import string

from collections import Counter


def read_data(input_file):
    """
    Reads the text in the input file, strips punctuation, and splits it into words.

    :param input_file: A text based file to read from.
    :return: A list of words.
    """

    with open(input_file, 'r') as in_file:
        data = in_file.read().split()
    return [word.translate(str.maketrans('', '', string.punctuation)) for word in data]


def build_dataset(wordlist, vocabulary_size):
    """
    Reads a wordlist and converts it to datastructures around their frequency

    :param wordlist: A list of words.
    :param vocabulary_size: The size of the vocabulary you want to consider. It will only output a dataset with the
                            vocabulary_size - 1 most frequent words from your wordlist.
    :return: A tuple of (words_and_frequency, words_to_index).
             words_and_frequency is a list of tuples of words and their frequency, ordered by frequency. The exception
                to this is that the last entry is a placeholder for all unknown words, that is, words from your wordlist
                that are less frequent than the top vocabulary_size - 1 words.
             words_to_index is a dictionary of words to their index in the words_and_frequency list.
    """
    counter = Counter(wordlist)
    words_and_frequency = counter.most_common(vocabulary_size - 1)
    words_to_index = {word_and_frequency[0]: index for index, word_and_frequency in enumerate(words_and_frequency)}

    unknown_count = sum(word not in words_to_index for word in wordlist)
    words_and_frequency.append(('UNKNOWN', unknown_count))
    words_to_index['UNKNOWN'] = len(words_and_frequency) - 1

    return words_and_frequency, words_to_index
