import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")

custome_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custome_tokenizer.tokenize(train_text)
for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    namedEnt.draw()