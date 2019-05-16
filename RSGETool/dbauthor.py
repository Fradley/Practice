import datetime
from mongoengine import *
connect('rsgedb', host='localhost', port=27017)

class Post(Document):
	itemid = IntegerField(required=True)
	itemname = StringField(required=True)
	buylimit = IntegerField(required=False)
	highalch = IntegerField(required=False)
	lowalch = IntegerField(required=False)
	price = IntegerField(required=True)
	updated = DataTimeField(default=datetime.datetime.now)
