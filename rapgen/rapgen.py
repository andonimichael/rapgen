from argparser import create_arg_parser

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    with open(args.input_file, 'r') as input_file, open(args.output_file, 'w') as output_file:
        for input_line in input_file:
            output_file.write(input_line)
