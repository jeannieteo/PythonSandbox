my_list = [8, 9, 6, 2, 4, 7, 0]  # list to sort
#go=True
for x in range(len(my_list) - 1):
#while go:
    ##go = False
    for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
        if my_list[i] > my_list[i + 1]:  # compare adjacent elements
           # go = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
    print(my_list)   