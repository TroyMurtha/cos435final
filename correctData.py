import json
from stdEvent import stdEvent
from stdEvent import categories
import pickle
import sklearn



# Load Training Data
events = open('./data/events.pckl', 'r');
trainingData = pickle.load(events)

# Loop through, allowing the user to correct or remove errors
for i in range (0, len(trainingData)) :
    if (0 == trainingData[i].category) :
        print "Title:\t{}".format(trainingData[i].name)
        print "Description:\t{}".format(trainingData[i].description)
        print "\n{}\n".format(categories)
        category =  int(input("Category: "))
        trainingData[i].category = category

events = open('./data/events.pckl', 'w');
pickle.dump(trainingData, events)
events.close()
