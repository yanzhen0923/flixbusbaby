import nltk
from nltk.collocations import *
from nltk.tokenize import TweetTokenizer
import ast

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

with open('flixbus_review.txt') as f:
    lines = f.readlines()

with open('two_words_word_2.txt', 'a+') as f:
        
    tknzr = TweetTokenizer()
    i = 0
    for l in lines:
        i += 1
        print(i)
        dict_word = ast.literal_eval(l)
        res = tknzr.tokenize(dict_word['review'])
        two_words = ''
        for i in range(len(res) - 1):
            if ((i & 1) == 0):
                two_words += (res[i] + res[i + 1] + ' ')
        dict = {'review': two_words, 'stars': dict_word['stars']}
        f.write("%s\n" % dict)
    f.close()
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
