import nltk
from nltk.collocations import *
from nltk.tokenize import TweetTokenizer
import ast

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()


with open('flixbus_review.txt') as f:
    lines = f.readlines()

with open('two_words_word_1', 'a+') as f:
        

    tknzr = TweetTokenizer()
    tmp = 'tmp.txt'
    i = 0
    for l in lines:
        i += 1
        print(i)
        dict_word = ast.literal_eval(l)
        res = tknzr.tokenize(dict_word['review'])
        two_words = ''
        for i in range(len(res)):
            if ((i & 1)):
                two_words += (res[i - 1] + res[i] + ' ')
        print(two_words)
    # change this to read in your data
    # with open(tmp, 'w+') as fw:
    #    fw.write(dict_word['review'])
    #    fw.close()

    #with open(tmp, 'r') as fw:
    #    new_line = fw.readlines()
    #    print(new_line)
    #    fw.close()

    #finder = BigramCollocationFinder.from_words(
    #    nltk.corpus.genesis.words(tmp))
# only bigrams that appear 3+ times
    #finder.apply_freq_filter(0) 
# return the 10 n-grams with the highest PMI
    #b = finder.nbest(bigram_measures.pmi, 20) 
    #print(b)
