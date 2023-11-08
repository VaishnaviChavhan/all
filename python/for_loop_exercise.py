            # average 

# heights = input("Enter the heights: ")
# height_list=heights.split()
# count=0
# for height in height_list:
#     count = count + 1
# print(count)
# for i in range(count):
#     height_list[i] = int(height_list[i])
# print(height_list)
# total=0
# for i in height_list:
#     total=total+i
#     average = total/count
# print(round(average))


                # maximum number

numbers=input("Enter the list of numbers: ")
number_list=numbers.split()
count=0
for i in number_list:
    count = count + 1
print(f"The lenght of the list is :{count}")
for i in range(count):
    number_list[i]=int(number_list[i])
maximum_number = 0
for i in number_list:
    if i >maximum_number:
        maximum_number=i
print(f"The maximum number is: {maximum_number}")