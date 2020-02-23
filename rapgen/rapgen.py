import gensim
import logging

from argparser import create_arg_parser
from directory_reader import DirectoryReader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    data_reader = DirectoryReader(args.input_directory)
    model = gensim.models.Word2Vec(data_reader,
                                   size=args.dimensions,
                                   window=args.window_size,
                                   min_count=args.min_count,
                                   max_vocab_size=args.vocab_size,
                                   sg=1)
    model.save(args.output_file)

    wv = model.wv

    vocab_stats = [(word, vocab.count, vocab.index) for word, vocab in wv.vocab.items()]
    logging.info(vocab_stats[:10])
    for word, _, _ in vocab_stats[:10]:
        logging.info(wv.most_similar(word))
