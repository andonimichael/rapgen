from argparse import ArgumentParser, ArgumentTypeError


def create_arg_parser():
    """ Creates an argument parser that handles input and output file names and vocabulary size. """

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
                                 '--input',
                                 dest='input_file',
                                 help='The input file',
                                 required=True)
    cmd_line_parser.add_argument('-o',
                                 '--output',
                                 dest='output_file',
                                 help='The output file',
                                 required=True)
    cmd_line_parser.add_argument('--vocabsize',
                                 type=positive_integer,
                                 dest='vocab_size',
                                 help='The size of the model\'s vocabulary',
                                 default=50000,
                                 required=False)
    return cmd_line_parser
