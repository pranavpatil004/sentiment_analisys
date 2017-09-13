from nltk.stem import WordNetLemmatizer
import nltk


lemmatizer = WordNetLemmatizer()


print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
words = nltk.word_tokenize("better")
print(nltk.pos_tag(words)[0][1])
print(lemmatizer.lemmatize("better", pos='a'))

print(lemmatizer.lemmatize("had", pos="v"))

