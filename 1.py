
def sum(n):
    total = 0
    for index in range(n+1):
        total += index
        print(index)
    return total


# A list is an ordered collection of items. Python uses the square brackets ([]) to indicate a list.
# Write a Python program to get the largest number from a list.

def BiggestInList( list ):
    Biggest = 0
    for index in range(len(list)):
        if (Biggest < list[index]):
            Biggest = list[index]
    print(Biggest)

BiggestInList([1,34,5,7,89,9,88])

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

print(max_num_in_list([1, 2, -8, 0]))
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
print(min(nums))

# Write a Python program remove any number > 5 and any space from a list

def str_to_list(str) :
    list = []
    listcopy = []
    list[:0] = str
    listcopy[:0] = str
    for x in listcopy:
        if x.isdigit():
            if int(x) > 5:
                list.remove(x)
        if x.isspace():
                list.remove(x)
    return list

str1 = "6 cents"
print(str_to_list(str1))

# Write a Python program reverse words of a given string
string = "geeks quiz practice code no"
s = string.split()
index = -1
for i in s:
    print(s[index], end =" ")
    index = index-1

with open('file_to_save.txt', 'w') as open_file:
    open_file.write('A string to write2')

def is_year_leap(year):
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            return True
        if (year % 100 == 0) and (year % 400 > 0):
            return False
        else:
            return True
    else:
        return False