# total = 0
# for i in range(1,101):
#     total+=i
# print(total)


# a = range(0,10,1)
# for i in a:
#     print(i)

# a = range(0,-10,-1)
# for i in a:
#     print(i)


# a=range(-1,-10,-1)
# for i in a:
#     print(i)


# a=range(10,0,-1)
# for i in a:
#     print(i)



                        # Exercise

# a=range(2,100,2)
# for i in a:
#     print(i)


# number = int(input("Enter the Numbers: "))
# for i in range(number):
#     if i%2==0:
#         print(i)
    


                        # Exercise
number =int(input("Enter the number: "))
for i in range(1,number):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)