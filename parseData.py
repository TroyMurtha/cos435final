import json
from stdEvent import stdEvent
from stdEvent import categories
import pickle

translation = {'0' : 0, '1'  : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}

def setTranslatingScheme (scheme) :
    for i in length(scheme) :
        i    
def transate (intToBeTranslated) :
    return translation[str(intToBeTranslated)]



#Training Data
trainingData = []

# Load Princeton Public Events Calendar
ppec = json.load(open('./data/ppec'))

# Parse Princeton Data
for event in ppec['events'] :
    name = event['title']
    description = event['description']
    if (len(event['categories']) > 0) :
        category = event['categories'][0]['categoryID']
    else :
        category = 0
    parsedEvent = stdEvent(name, description, category)
    trainingData.append(parsedEvent)


# MIT data

mit = pickle.load(open('./data/mit', 'r'))

for event in mit :
    name = event['title']
    description = event['summary']
    category = 0
    parsedEvent = stdEvent(name, description, category)
    trainingData.append(parsedEvent)

# Save it for posterity
events = open('./data/events.pckl', 'w');
pickle.dump(trainingData, events)
events.close()
