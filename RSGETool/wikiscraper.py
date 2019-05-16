import requests
from numpy import NaN
import datetime as datetime
from bs4 import BeautifulSoup
import re
import locale


def getInfo(url):

	item = requests.get(url)
	item = BeautifulSoup(item.text, 'html.parser')
	
	itemdata = {'itemid'	: NaN,
							'itemname': '',
							'buylimit': NaN,
							'highalch': NaN,
							'lowalch'	: NaN,
							'price'		: NaN,
							'updated'	: datetime.datetime.now
							}
	
	locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
	
	#grab values from the html
	itemdata['itemid'] = int(item.find(id='exchange-itemid').text)
	itemdata['itemname'] = item.find(class_='gemw-name').text
	itemdata['highalch'] = int(locale.atoi(item.find(id='exchange-highalch').text))
	itemdata['lowalch'] = int(locale.atoi(item.find(id='exchange-lowalch').text))
	itemdata['price'] = int(locale.atoi(item.find(class_='gemw-price').text))
	
	date = item.find(class_='gemw-updated')['data-date']
	
	#Fix when able to tell if month is given as Aug or August
	try:
		dt = datetime.datetime.strptime(date, '%d %b %Y, %H:%M (%Z)')
	except ValueError:
		dt = datetime.datetime.strptime(date, '%d %B %Y, %H:%M (%Z)')
		
	
	itemdata['updated'] = dt
	itemdata['buylimit'] = int(locale.atoi(item.find(id='exchange-limit').text))
	
	
	
	return itemdata
	

