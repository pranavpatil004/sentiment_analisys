from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.sentiment_analyzer import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))

stop_words = set(stopwords.words('english'))
words = word_tokenize(EXAMPLE_TEXT)

new_sentence = []

for word in words:
    if word not in stop_words:
        new_sentence.append(word)

print(new_sentence)

sid = SentimentIntensityAnalyzer()
for sentence in new_sentence:
     var1 = 0
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]))
         if k == "pos":
                        var1 += 1

print (var1)
