from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print(syns)
print(syns[0].lemmas())


print(syns[0].definition())

print(syns[0].examples())


synonims = []
antonyms = []

for syn in wordnet.synsets("good"):
    print("syn: ", syn)
    for l in syn.lemmas():
        print("l:",l)
        synonims.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


print (set(synonims))
print (set(antonyms))

w1 = wordnet.synset("boat.n.01")
w2 = wordnet.synset("ship.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("boat.n.01")
w2 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("boat.n.01")
w2 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("website.n.01")
w2 = wordnet.synset("site.n.01")

print(w1.wup_similarity(w2))