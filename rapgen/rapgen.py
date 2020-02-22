from argparser import create_arg_parser
from data_handler import build_dataset, read_data

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    wordlist = read_data(args.input_file)
    words_and_frequency, words_to_index = build_dataset(wordlist, args.vocab_size)

    with open(args.output_file, 'w') as output_file:
        output_file.write(str(wordlist) + '\n')
        output_file.write(str(words_and_frequency) + '\n')
        output_file.write(str(words_to_index) + '\n')
