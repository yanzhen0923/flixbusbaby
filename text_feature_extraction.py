import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("yelp_FlixBus_data.txt")
lines = file1.readlines()# Use this to read file content as a stream:
appendFile = open('filteredtext.txt','a+')
for line in lines:
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile.write(" "+r)
    appendFile.write("\n")
appendFile.close()

