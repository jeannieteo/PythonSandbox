
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

#BiggestInList([1,34,5,7,89,9,88])

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

#print(max_num_in_list([1, 2, -8, 0]))
#nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
#print(min(nums))

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

#str1 = "6 cents"
#print(str_to_list(str1))

# Write a Python program reverse words of a given string
def string_split(stringSplit):
    s = stringSplit.split()
    index = -1
    for i in s:
        print(s[index], end =" ")
        index = index-1
string_split("geeks quiz practice code no") 

#with open('file_to_save.txt', 'w') as open_file:
#    open_file.write('A string to write2')

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

def dict_print(dictionary):

    for key in sorted(dictionary.keys()):
        print(key, "->", dictionary[key])
    
    #Another way is based on using a dictionary's method named items(). 
    #The method returns tuples where each tuple is a key-value pair.
    for english, french in dictionary.items():
        print(english, "->", french)
    #There is also a method named values() returns values.
    for french in dictionary.values():
        print(french)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval", "apple":"appel"}
dict_print(dictionary)

#The default except branch must be the last except branch. Always!
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')

def any():
    print(var +1, end='')

var=1
any()
print(var)