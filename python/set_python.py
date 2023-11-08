# set1={10,56,89,90,'jenny',True}
# set2=set()
# set1.add(98)
# set1.remove(56)
# set1.clear()
# set1.discard(90)
# set1.pop()
# print(set1.pop())
# set1.add((13,14,15))
# set1.add([13,14,15])
# print(set1)
# print(type(set1))

                    # Questions on sets #
set1={'Ram','Shyam','Jenny'}
set2={'Jenny','Jiya','Akash'}
set3={'Ankur','Pradeep'}
# print(set1.union(set2,set3))
# print(set1|set2|set3)
# print(set2.union(set1,set3))
# print(set1.union(('Mohan','Jenny')))
# set1.update(set2)
# set1.update(['Jenny','Mohan'])
# set1|=set2
# print(set1)


# print(set1.intersection(set2))
# print(set1 & set2)
# set2.intersection_update(set1)
# print(set1)
# print(set2)


# print(set1.difference(set2))
# print(set1.difference(('Mohan','Shiva')))
# print(set1.difference(set2,set3))
# print(set1-set2)
# set1.difference_update(set2)
# print(set1)
# print(set2)
# print(set1.symmetric_difference(set2))
# print(set1^set2^set3)
# set2.symmetric_difference_update(set1)
# set1.symmetric_difference_update(('Mohan','Shiva'))
# print(set2)
# print(set1)


# print(set1.isdisjoint(set2))   #disjoint means noone is same in set
# print(set1.issubset(set2))        #subset means set1 have set2 
# print(set1<=set2)                     # subset
# print(set1>=set2)                        #superset
# print(set1.issuperset(set2))   # superset means set1 have all elements of set2
# set2.clear()
del set2
print(set2)