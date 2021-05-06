import nltk
import pyfpgrowth

with open('C:/Users/alireza/Desktop/retail.dat') as f:
    content = f.readlines()
content = [x.strip() for x  in content]
print(content)
sale = []
for i in range (0 , len(content)):
    sale.append(nltk.word_tokenize(content[i]))
#print(len(sale))
#print(len(content))
#print(sale)

patterns = pyfpgrowth.find_frequent_patterns(sale,300)
rules = pyfpgrowth.generate_association_rules(patterns, 0.8)

print(patterns)
print(rules)