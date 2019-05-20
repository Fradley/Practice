from pymongo import MongoClient
import wikiscraper
import datetime
import time

client = MongoClient('localhost', 27017)
db = client['itemdb']
coll = db.items
cursor = coll.find({})

count = coll.count_documents({})

ticker = 0.0

ts = time.time()

for doc in cursor:
	ticker += 1

	url = doc['url']
	oid = doc['_id']
	price = wikiscraper.getItemPrice(url)
	date = datetime.datetime.now
	tn = time.time() - ts
	if price:
		coll.update({'_id', oid}, {'$push': {'series': (date, price)}})
		
	if ticker % 10 == 0:
		pcnt = int((ticker / count) * 100)
		elapsed = int(tn)
		estlen = int((count / ticker) * tn)
		s = str(pcnt) + " % complete.\tElapsed: " + str(elapsed) + "\tETA: " + str(datetime.timedelta(seconds=(estlen - elapsed)))
		print(s)
