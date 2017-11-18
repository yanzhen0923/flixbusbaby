import urllib.request
from bs4 import BeautifulSoup

page = 1

f = open("yelp_BoltBus_data.txt", "a+")

# List of yelp urls to scrape
url = 'https://www.yelp.com/biz/boltbus-san-francisco-2?osq=bus'

for i in range(page):
    data_i = urllib.request.urlopen(url).read()
    soup_i = BeautifulSoup(data_i, 'lxml')

    # get reviews in a list
    reviews = soup_i.findAll("div", {"class": 'review-content'})
    # extract the actual text
    text_reviews = []
    for r in reviews:
        # find content in <p lang "en"> </p>
        text_reviews.append(r.find('p').text)

    # get ratings in a list
    ratings = soup_i.findAll("div", {"class": 'i-stars'})

    num_ratings = []
    for r in ratings:
        # find in string the indication in order to find the rating number
        num = str(r).find('title="')
        # rating number in format x.x
        rate = str(r)[int(num+7)]
        rate = rate + str(r)[int(num+8)]
        rate = rate + str(r)[int(num+9)]
        # add rating to list
        num_ratings.append(rate)
    # remove the first rating, cause its something else
    num_ratings.pop(0)
    # remove the last 4 ratings
    current_list_l = len(num_ratings)
    for i in range(1,5):
        num_ratings.pop(current_list_l - i)

    for i in range(len(text_reviews)):
        dict = {}
        dict['review'] = text_reviews[i]
        dict['stars'] = num_ratings[i]
        f.write('%s\n' % dict)

f.close()