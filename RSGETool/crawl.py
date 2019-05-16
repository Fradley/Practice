import wikiscraper

baseurl = 'https://runescape.wiki/w/RuneScape:Grand_Exchange_Market_Watch/Rune_Index'

prefix =  'https://runescape.wiki'

pagepattern = r'w\/RuneScape:Grand_Exchange_Market_Watch\/'

itempattern = r'w\/Exchange:'

catlinks = wikiscraper.getLinks(baseurl, prefix, pagepattern)

itemlinks = []

for link in catlinks[0:10]:
	itemlinks.append(wikiscraper.getLinks(link, prefix, itempattern))
	
print(itemlinks)
