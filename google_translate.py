from googletrans import Translator
import ast
translator = Translator()

#res = translator.translate('这个可以有')
#print(res.text)

with open('data_trustpilot.txt') as f:
    lines = f.readlines()

fw = open("trustpilot_english.txt", "a+")
i = 0
for l in lines:
    i += 1
    print(i)
    dict = ast.literal_eval(l)
    org_text = dict['review']
    try:
        new_text = translator.translate(org_text).text
    except:
        print('oooo')
        continue
    new_dict = {'review': new_text, 'stars': dict['stars']}
    fw.write('%s\n' % new_dict)
