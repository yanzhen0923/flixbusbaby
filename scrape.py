#File to scrape English speaking reviews from 
#https://www.tripadvisor.com/ShowUserReviews-g196638-d12232500-r541544545-Flixbus-Tourcoing_Nord_Hauts_de_France.html
#for Flixbus and save it into a txt. The URLs of all the pages containing the reviews are in the separate urls.py file in a list

import requests
from bs4 import BeautifulSoup as Soup
from urls import urls as urls

def scrape(url):

	page = requests.get(url)

	if(page.status_code != 200):
		print("Error downloading the page")
		return false

	sp = Soup(page.content, 'html.parser')


	#All divs containing a single review
	revDiv = sp.find_all('div', class_='review-container')

	for i in range(0, len(revDiv)):
		review = {}
		review['review'] = revDiv[i].find('p', class_='partial_entry')

		#Finding what rating from 1-5 was given for the current review
		if(revDiv[i].find('span', class_='ui_bubble_rating bubble_10')):
			review['stars'] = 1
		
		if(revDiv[i].find('span', class_='ui_bubble_rating bubble_20')):
			review['stars'] = 2
		
		if(revDiv[i].find('span', class_='ui_bubble_rating bubble_30')):
			review['stars'] = 3
		
		if(revDiv[i].find('span', class_='ui_bubble_rating bubble_40')):
			review['stars'] = 4
		
		if(revDiv[i].find('span', class_='ui_bubble_rating bubble_50')):
			review['stars'] = 5
		
		reviews.append(review)

#A list of dictionaries containing all the reviews and the corresponding ratings
reviews = []

#Getting the reviews and ratings for all the URLs
for i in range(0, len(urls)):
	scrape(urls[i])

#Saving the result into a txt
thefile = open('reviews.txt', 'w')

for item in reviews:
  thefile.write("%s\n" % item)

