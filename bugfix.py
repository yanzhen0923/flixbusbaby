import string
with open('yelp_Megabus_NewYork_data.txt') as f:
    lines = f.read()

res = string.replace(lines, "\\xa0", "")

with open('yelp_Megabus_NewYork_data_fix.txt', 'a+') as ff:
    ff.write(res)
