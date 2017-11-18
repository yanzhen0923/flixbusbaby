import nltk
import io

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
f = io.open('alldata.txt', 'rU', encoding='utf-8')
lines = f.read() 
lines = lines.lower()
words = nltk.word_tokenize(lines) 

taggedWords = nltk.pos_tag(words)


#print(list(nltk.bigrams(words)))
adjectiveList = {word for word, pos in taggedWords if pos.startswith('JJ')}
adjectiveList = [word.lower() for word in adjectiveList]

#pairs=nltk.bigrams(words)
#bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()
#finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
#finder.apply_freq_filter(3)
#finder.nbest(bigram_measures.pmi, 10)


#print(pairs)

fdist = nltk.FreqDist(adjectiveList)


for word, frequency in fdist.most_common(20):
	print(u'{} - {}'.format(word, frequency))
