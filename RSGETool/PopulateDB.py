import pickle
import wikiscraper
import time
import requests
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['itemdb']

items = pickle.load(open('items.p', 'rb'))

#remove duplicate items
items = set(items)

count = len(items)

ticker = 0.0

ts = time.time()
for item in items:
	ticker += 1

	try:
		post = wikiscraper.getInfo(item)
	except requests.exceptions.ConnectionError:
		print('bad link ' + link)
		
	db.posts.insert_one(post)
	
	pcnt = int((ticker / count) * 100.0)
	tn = time.time() - ts
	if ticker % 10 == 0:
		s = str(pcnt) + " % complete. ETA: " + str(int(tn / (ticker / count)))
		print(s)
