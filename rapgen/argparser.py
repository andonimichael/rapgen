from argparse import ArgumentParser


def create_arg_parser():
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
    return cmd_line_parser
