import nltk
import io
import re
from collections import Counter

## Irrelevant stuff ##
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#f = io.open('alldata.txt', 'rU', encoding='utf-8')
#lines = f.read() 
#lines = lines.lower()
#words = nltk.word_tokenize(lines) 

#taggedWords = nltk.pos_tag(words)


#print(list(nltk.bigrams(words)))
#adjectiveList = {word for word, pos in taggedWords if pos.startswith('JJ')}
#adjectiveList = [word.lower() for word in adjectiveList]

#pairs=nltk.bigrams(words)
#bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()
#finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
#finder.apply_freq_filter(3)
#finder.nbest(bigram_measures.pmi, 10)


#print(pairs)

#fdist = nltk.FreqDist(adjectiveList)


#for word, frequency in fdist.most_common(20):
#	print(u'{} - {}'.format(word, frequency))
##END of irrelevant stuff##

#Feature list expected by countWordOcc
#features = ['wifi', 'driver', 'toilet', 'online', 'internet']
text = open('supervised_training_data.txt').read()
features = text.split(';')

#Function to count the occurrence of a list of words in the data
def countWordOcc(file, featureList):
    
    cnt = Counter()
    words = re.findall('\w+', open(file).read().lower())
    for word in words:
        if word in featureList and len(word) > 1:
            cnt[word] += 1
        
    #length = len(words)
    average = 200000 / 3074
    with open(file) as f:
        for line_count, l in enumerate(f):
            pass
    line_count += 1
    length = line_count * average
    percent_cnt = Counter()
    for word in featureList:
        #print(cnt[word])
        percentage = (cnt[word] / length) * 100
        percent_cnt[word] = percentage

    print(cnt)
    print(percent_cnt)



countWordOcc("megabus.txt", features)
