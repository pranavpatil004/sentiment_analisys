from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


i = "This is an example for stemming for the sentences having stemming words in it"

ps = PorterStemmer()

words = word_tokenize(i)

for j in words:
    print (ps.stem(j))