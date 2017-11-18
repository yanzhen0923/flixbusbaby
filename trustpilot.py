import urllib.request

from bs4 import BeautifulSoup

f=open("data_trustpilot.txt", "a+")

base_url = 'https://de.trustpilot.com/review/flixbus.com?languages=all&page='

for i in range(67):
    req_url = base_url + str(i + 1)
    data_i = urllib.request.urlopen(req_url).read()
    print(i)
    soup_i = BeautifulSoup(data_i, 'lxml')
    reviews = soup_i.findAll("div", { "class" : "review-body" })
    ratings = soup_i.findAll("div", { "class" : "star-rating" })
    ratings.pop(0)
    num_ratings = []
    for r in ratings:
        num = str(r).find('count-')
        rate = str(r)[int(num + 6)]
        num_ratings.append(rate)
    
    for i in range(len(reviews)):
        dict = {}
        dict['review'] = reviews[i].text.strip()
        dict['stars'] = num_ratings[i]
        f.write('%s\n' % dict)
f.close()

#for r in reviews:
#    print(r.text)
    #print(r.cssselect('div'))
