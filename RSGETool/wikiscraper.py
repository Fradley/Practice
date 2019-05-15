import requests
from bs4 import BeautifulSoup

def getInfo(url):


	item = requests.get(url)
	item = BeautifulSoup(item)
	#item.find_all('span', class_= 'gemw-price')
	pass
	
