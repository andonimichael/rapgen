from argparser import create_arg_parser
from data_reader import read_data

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    data = read_data(args.input_file)

    with open(args.output_file, 'w') as output_file:
        output_file.write(str(data))
