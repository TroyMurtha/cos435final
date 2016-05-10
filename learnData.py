from stdEvent import stdEvent
from stdEvent import categoryNames
import pickle
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import cross_validation

# Load Data
events = open('./data/events.pckl', 'r');
trainingData = pickle.load(events)
# Turn the various categories into lists
names, targets, descriptions = [], [], []
for i in range (0, len(trainingData)) :
    names.append(trainingData[i].name)
    targets.append(trainingData[i].category)
    descriptions.append(trainingData[i].description)
# Make some vectors or something
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(descriptions)
# Lets fit it
clf = MultinomialNB(alpha=.01)
clf.fit(vectors, targets)
# Make some predictions
pred = clf.predict(vectors)
# Check how well we did we will use kfold cross validation
train_vectors, test_vectors, train_resp, test_resp = cross_validation.train_test_split(vectors, targets, test_size=0.2, random_state=0)
clf = MultinomialNB(alpha=.01)
clf.fit(train_vectors, train_resp)
# Make some predictions
pred = clf.predict(test_vectors)

print metrics.f1_score(test_resp, pred, average='weighted')

events.close()
