import json
from stdEvent import stdEvent
import pickle
import sklearn
from nltk.corpus import stopwords

#Training Data
events = open('./data/events.pckl', 'r');
trainingData = pickle.load(events)
cachedStopWords = stopwords.words("english")
for i in range (0, len(trainingData)) :
    # Add title to the desfription
    trainingData[i].description = ' '.join([trainingData[i].name, trainingData[i].description])
    # Remove Stop Words
    trainingData[i].description = ' '.join([word for word in trainingData[i].description.split() if word not in cachedStopWords])
    print trainingData[i].description
events.close()
