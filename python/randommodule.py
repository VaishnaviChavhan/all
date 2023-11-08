                # random module
# randint(a,b)   a<= X  <=b
# randrange(a,b) a<= X < b
# random()   0.0 <=  X <1.0
# uinform()
# choice()
# shuffle ()

# import random


# a=random.randint(1,3)
# print(a)

# a=random.randrange(1,3)
# print(a)

# a=random.random()
# print(a)

# a=random.uniform(1,3)
# print(a)

# l=[2,5,3,8,6,9,12,45]
# a=random.choice(l)
# print(a)


# random.shuffle()
# print(l)




import random

side=random.randint(0,1)
print(side)
if side==1:
    print("HEADS")
else:
    print("TAILS")