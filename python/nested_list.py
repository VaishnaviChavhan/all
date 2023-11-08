#list1=[10,34,20,[45,78,-3],89]
# print(len(list1))
# print(list1[3][2])
# print(list1[len(list1)-1])
# print(list[3][0:2])


# list2=[10,34,90,['Mohan','Shyam','Ram'],89]
# print(list2[3][2])


row1=['😘','😘','😘']
row2=['😘','😘','😘']
row3=['😘','😘','😘']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter the position where you want to hide money: ")
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='X'
print(f"{row1}\n{row2}\n{row3}")
