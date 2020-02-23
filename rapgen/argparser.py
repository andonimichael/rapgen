from argparse import ArgumentParser, ArgumentTypeError


def create_arg_parser():
    """ Creates an argument parser that handles an input directory, model output file, and vocabulary size. """

    def positive_integer(input_string):
        """ Validates that the input string is a positive integer. """
        try:
            value = int(input_string)
            if value > 0:
                return value
            else:
                raise ArgumentTypeError('Error: {} is not a positive integer'.format(input_string))
        except ValueError:
            raise ArgumentTypeError('Error: {} is not a valid integer'.format(input_string))

    cmd_line_parser = ArgumentParser()
    cmd_line_parser.add_argument('-i',
                                 '--input_directory',
                                 dest='input_directory',
                                 help='The input directory',
                                 required=True)
    cmd_line_parser.add_argument('-o',
                                 '--output',
                                 dest='output_file',
                                 help='The output file for the model',
                                 required=True)
    cmd_line_parser.add_argument('--window-size',
                                 type=positive_integer,
                                 dest='window_size',
                                 help='The number of surrounding words to consider in the model.',
                                 default=10,
                                 required=False)
    cmd_line_parser.add_argument('--min-count',
                                 type=positive_integer,
                                 dest='min_count',
                                 help='The minimum number of occurrences of a word for it to be included in the model.',
                                 default=1,
                                 required=False)
    cmd_line_parser.add_argument('--vocabsize',
                                 type=positive_integer,
                                 dest='vocab_size',
                                 help='The size of the model\'s vocabulary',
                                 default=50000,
                                 required=False)
    cmd_line_parser.add_argument('-d',
                                 '--dimensions',
                                 type=positive_integer,
                                 dest='dimensions',
                                 help='The dimensionality of the vector space to consider.',
                                 default=200,
                                 required=False)
    return cmd_line_parser
