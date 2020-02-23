# RapGen

This repo contains a rap generator based on Word2Vec and its extension, Doc2Vec. These are shallow neural nets trained against a corpus of popular rap songs, specially designed to provide context of words and their paragraphical structure. The hope is to reconstruct rhyme scheme, syllable consistency, and stanza lengths. A stretch goal will be to encompass choral sections.

It was decided to use Gensim over TensorFlow due to the ease of the API and clean abstraction between the business logic and the core ML machinery.

This tool is meant to work hand-in-hand with my [OHHLA Web Scraper](https://github.com/andonimichael/OHHLA-WebScraper); however, was built abstract enough to run over any directory containing a corpora of `.txt` files.

## Usage

```
python rapgen/rapgen.py -i <input_directory> -o <output_file> [--window-size <positive int>] [--min-count <positive int>] [--vocabsize <positive int>] [--dimensions <positive int>]
```
