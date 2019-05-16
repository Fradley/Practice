#	Planning Document


##	Scrape RS wiki for grand exchange prices  
*	  Ideally hourly resolution  
*		Need way to detect new items  


##	compile data into some kind of database  
*		~38,000 items  
*		Title | Price t1 | Price t2 | Price t3 | ... | Price tN |  
* 	MongoDB  


##	perform analytics on data  
*	  Time series analysis
*		Determine items most likely to yield a profit over time
*		Dynamically add and remove items from being watched (Don't need hourly data on stagnant items)
*		Run full pass weekly, find stagnant items
*		Could run NLP over patch notes and developer blogs to aid algorithms


## put list into a flask front-end
