from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize


sample = gutenberg.raw("bible-kjv.txt")
tokenized = sent_tokenize(sample)

print(tokenized[5:15])