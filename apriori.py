import Orange

data = Orange.data.Table("market-basket.basket")
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.3)
print(Orange.associate.print_rules(rules))
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:5]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)


for i in range(len(data)):
    print(data[i])


# how to create a dataset
# https://docs.orange.biolab.si/3/data-mining-library/reference/data.table.html 