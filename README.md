# RapGen

This repo contains a rap generator based on Word2Vec and its extension, Doc2Vec. These are shallow neural nets trained against a corpus of popular rap songs, specially designed to provide context of words and their paragraphical structure. The hope is to reconstruct rhyme scheme, syllable consistency, and stanza lengths. A stretch goal will be to encompass choral sections.

It was decided to use Gensim over TensorFlow due to the ease of the API and clean abstraction between the business logic and the core ML machinery. 
