import xlwt
import nltk
from xlrd import open_workbook
from nltk.tokenize import word_tokenize

# train = [("Great place to be when you are in Bangalore.", "pos"),
#                  ("The place was being renovated when I visited so the seating was limited.", "neg"),
#                  ("Loved the ambience, loved the food", "pos"),
#                  ("The food is delicious but not over the top.", "neg"),
#                  ("Service - Little slow, probably because too many people.", "neg"),
#                  ("The place is not easy to locate", "neg"),
#                  ("Mushroom fried rice was spicy", "pos"),
#                  ("Customer service", "Customer service"),
#                  ("Website slow to load", "Website slow to load"),
#                  ("Difficult to login", "Difficult to login"),
#                  ("Payment related", "Payment related"),
#                  ("Website related", "Website related"),
#                  ("Competitor mentioned", "Competitor mentioned"),
#
#
#                  ]



train = [("customer", "customer"),
                 ("account", "account"),
                 ("login", "login"),
                 ("payment", "payment"),
                 ("website", "website"),
                 ("competitor", "competitor"),
                 ("navigation navigate", "navigation"),



                 ]

# Step 2
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))

# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]


classifier = nltk.NaiveBayesClassifier.train(t)


workbook = open_workbook("voc.xlsx")
sheets = workbook.sheet_names()

bk = xlwt.Workbook()
sheet = bk.add_sheet("Classified data")
sheet.write(0, 0, "website")


required_data = []
for sheet_name in sheets:
    sh = workbook.sheet_by_name(sheet_name)
    for rownum in range(sh.nrows):
        row_valaues = sh.row_values(rownum)
      #  print row_valaues[8]
        #required_data.append((row_valaues[8], row_valaues[8]))
        test_data = row_valaues[8]
        test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
        if classifier.classify(test_data_features) == "website" :
            print (test_data_features)
            print (classifier.classify(test_data_features))
            #sheet.write(0,1,row_valaues[8])

        if classifier.classify(test_data_features) == "login":
            print (test_data_features)
            print (classifier.classify(test_data_features))


        if classifier.classify(test_data_features) == "customer" :
            print (test_data_features)
            print (classifier.classify(test_data_features))


        if classifier.classify(test_data_features) == "navigation":
            print (test_data_features)
            print (classifier.classify(test_data_features))


        if classifier.classify(test_data_features) == "account":
            print (test_data_features)
            print (classifier.classify(test_data_features))








bk.save('classification.xls')