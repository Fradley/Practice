from pymongo import MongoClient
import wikiscraper
import datetime

client = MongoClient('localhost', 27017)
db = client['itemdb']
coll = db.items
cursor = coll.find({})

count = coll.count_documents()

ticker = 0.0


for doc in cursor:
	ticker += 1

	url = doc['url']
	oid = doc['_id']
	price = wikiscraper.getItemPrice(url)
	date = datetime.datetime.now
	
	if price:
		coll.update_one({'_id', oid}, {'$push': {'series': (date, price)}})
		
	if ticker % 10 == 0:
		elapsed = int(tn)
		estlen = int((count / ticker) * tn)
		s = str(pcnt) + " % complete.\tElapsed: " + str(elapsed) + "\tETA: " + str(datetime.timedelta(seconds=(estlen - elapsed)))
		print(s)
