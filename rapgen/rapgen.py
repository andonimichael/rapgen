import gensim
import logging

from argparser import create_arg_parser
from directory_reader import DirectoryReader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()

    data_reader = DirectoryReader(args.input_directory)
    words_and_phrases = gensim.models.Phrases(data_reader, max_vocab_size=args.vocab_size)
    model = gensim.models.Word2Vec(words_and_phrases[data_reader],
                                   size=args.dimensions,
                                   window=args.window_size,
                                   min_count=args.min_count,
                                   max_vocab_size=args.vocab_size,
                                   sg=1)
    model.save(args.output_file)

    word_vectors = model.wv

    vocab_stats = [(word, vocab.count, vocab.index) for word, vocab in word_vectors.vocab.items()]
    for word, _, _ in vocab_stats[:10]:
        logging.info(f'{word}: {word_vectors.most_similar(word)}')
