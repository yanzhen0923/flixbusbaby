from googletrans import Translator
import ast
translator = Translator()

#res = translator.translate('这个可以有')
#print(res.text)

with open('flixbus_review_filtered.txt') as f:
    lines = f.readlines()

f1 = open('flixbus_review_filtered_rate_1.txt', 'a+') 
f2 = open('flixbus_review_filtered_rate_2.txt', 'a+') 
f3 = open('flixbus_review_filtered_rate_3.txt', 'a+') 
f4 = open('flixbus_review_filtered_rate_4.txt', 'a+') 
f5 = open('flixbus_review_filtered_rate_5.txt', 'a+') 


rate_list_1 = []
rate_list_2 = []
rate_list_3 = []
rate_list_4 = []
rate_list_5 = []
i = 0
for l in lines:
    i += 1
    print(l)
    dict_word_ratings = ast.literal_eval(l)
    org_text = dict_word_ratings['review']
    ratings = dict_word_ratings['stars']

    if ratings == '1' or ratings == '1.0':
        f1.write('%s\n' % dict_word_ratings)
    if ratings == '2':
        f2.write('%s\n' % dict_word_ratings)
    if ratings == '3':
        f3.write('%s\n'% dict_word_ratings)
    if ratings == '4':
        f4.write('%s\n'% dict_word_ratings)
    if ratings == '5':
        f5.write('%s\n'% dict_word_ratings)
