import nltk
from nltk.tokenize import word_tokenize
str1 = 'Hell'
str2 = 'HelloWorld...zzzzzz11'
if(str1 in str2):
    print("I'm here")

train = [("Great place to be when you are in Bangalore.", "pos"),
("The place was being renovated when I visited so the seating was limited.", "neg"),
("Loved the ambience, loved the food", "pos"),
("The food is delicious but not over the top.", "neg"),
("Service - Little slow, probably because too many people.", "neg"),
("The place is not easy to locate", "neg"),
("Mushroom fried rice was spicy", "pos"),
("The chapati was too hot", "neg"),
]

# Step 2
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))

# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]


classifier = nltk.NaiveBayesClassifier.train(t)

test_data = "I wouldnt say that the Manchurian was too hot but I loved the food"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}

print (classifier.classify(test_data_features))