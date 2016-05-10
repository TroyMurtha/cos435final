import json
import sys
import feedparser
import pickle

# Given an address that corresponds to a json, downloads the json and returns it as a dictionary
address = sys.argv[1]
d = feedparser.parse(address)
# Now save it
filename = '/'.join(['./data', sys.argv[2]])
fileToBeSaved = open(filename, 'w')
pickle.dump(d['entries'], fileToBeSaved)
fileToBeSaved.close()
