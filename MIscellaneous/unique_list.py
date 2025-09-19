my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

list2 =[]
for x in range(len(my_list)-1):
    if my_list[x] not in list2:
        list2.append(my_list[x])
print("The list with unique elements only:")
print(list2)