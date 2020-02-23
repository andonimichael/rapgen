import os
import string


class DirectoryReader:
    """
    Reads the text of each '.txt.' file in the input directory, strips punctuation, and splits it into words. This
    streams the results into a generator rather than fetching all text into memory at once.
    """
    def __init__(self, directory_name):
        """
        :param directory_name: The directory containing a corpora of text files.
        """
        self.directory_name = directory_name

    def __iter__(self):
        """
        :return: A generator of sanitized words.
        """
        for file_name in filter(lambda f: f.endswith('.txt'), os.listdir(self.directory_name)):
            with open(os.path.join(self.directory_name, file_name)) as file:
                for line in file:
                    words = line.split()
                    yield [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
