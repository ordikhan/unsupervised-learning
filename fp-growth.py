import pyfpgrowth

'''transactions = [
    ['A', 'B'],
    ['B', 'D'],
    ['B', 'C', 'E'],
    ['C', 'D'],
    ['A', 'C', 'E'],
    ['A', 'D', 'E'],
    ['B', 'A', 'E'],
    ['C', 'A'],
    ['A', 'D', 'E'],
    ['A', 'B', 'E']
]
'''

fname = 'C:/Users/e.almaee/Desktop/Dataset/retail.dat'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like \n at the end of each line
content = [x.strip() for x in content]

transactions = []
for c in content:
    t = []
    for w in c.split():
        t.append(w)
    transactions.append(t)

transactions = transactions[0:400]


patterns = pyfpgrowth.find_frequent_patterns(transactions, 10)
rules = pyfpgrowth.generate_association_rules(patterns, 0.50)

#print(patterns)
print(rules)


