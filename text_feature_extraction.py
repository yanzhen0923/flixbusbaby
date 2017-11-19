import io
from nltk.corpus import stopwords
import ast
import collections
import difflib
from nltk.tokenize import word_tokenize

#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("yelp_BoltBus_NewYork_data.txt")
lines = file1.readlines()# Use this to read file content as a stream:
appendFile = open('filteredtext.txt','w')
for line in lines:
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile.write(r+" ")
    appendFile.write("\n")
appendFile.close()

with open('filteredtext.txt') as f:
    data1 = f.readlines()

# create rating dict with list
rating_cluster = {}
rating_keyword = {}
total_keyword_appearence = {}
for r in range(1,6):
    rating_cluster[r] = []
    rating_keyword[r] = []
    total_keyword_appearence[r] = []

for rating in range(1,6):
    # read every line of data as dict
    for l in data1:
        data_dict = ast.literal_eval(l)

    # classify according to ratings
        comment_list = []
        if int(float(data_dict['stars'])) == rating:
            rating_cluster[rating].append(data_dict['review'].lower())

#print(rating_cluster)


# read classes
keyword = open('supervised_training_data.txt')
key_cluster = keyword.read().split(';')

# find most common keywords in comments
for r in range(1,6):
    for comment in rating_cluster[r]:
        # find keyword in comment
        for word in key_cluster:
            # if keyword is in comment
            if comment.find(word) != -1:
                total_keyword_appearence[r].append(word)

    counter = collections.Counter(total_keyword_appearence[r])
    rating_keyword[r] = counter.most_common(10)

print(rating_keyword)




