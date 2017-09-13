from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This is an example of stop word filtration"

tokenized = word_tokenize(example)
stop_words = set(stopwords.words("english"))

print (stop_words)

if(stop_words.__contains__("off")):
    print("Contains")
filter = []

for i in tokenized:
    if i not in stop_words:
        filter.append(i)

print (filter)