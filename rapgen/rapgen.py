import logging

from argparser import create_arg_parser
from data_handler import build_dataset
from directory_reader import DirectoryReader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    data_reader = DirectoryReader(args.input_directory)
    wordlist = [word for words in data_reader for word in words]  # Just for backwards compat until we leverage Genisim
    words_and_frequency, words_to_index = build_dataset(wordlist, args.vocab_size)

    with open(args.output_file, 'w') as output_file:
        output_file.write(str(wordlist) + '\n')
        output_file.write(str(words_and_frequency) + '\n')
        output_file.write(str(words_to_index) + '\n')
