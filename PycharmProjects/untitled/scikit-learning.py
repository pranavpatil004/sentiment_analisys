import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
import pickle
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]


random.shuffle(documents)

# print (documents[0])

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print (all_words.most_common(15))

# print (all_words["stupid"])

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
         features[w] = (w in words)

    return features

# print ((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featureset = [(find_features(rev), category) for (rev, category) in documents]

print("Featureset = ", featureset)

training_set = featureset[:1900]
testing_set = featureset[1900:]

# classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f =  open("nive.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print ("Original Naive Bays Accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print ("MNB Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

# Gaussian_classifier = SklearnClassifier(GaussianNB())
# Gaussian_classifier.train(training_set)
# print ("Gaussian Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy(Gaussian_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print ("Bernoulli Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)



SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print ("SVC Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print ("LinearSVC Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print ("NuSVC Classifier Naive Bays Accuracy: ", (nltk.classify.accuracy( NuSVC_classifier, testing_set))*100)