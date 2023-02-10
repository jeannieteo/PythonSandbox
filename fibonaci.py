def fibonaci(num): #every number is sum of 2 preceding number
    fibolist = [0, 1, 1]
    total = 2
    if num < 1:
        return None
    if num <=2:
        return 1
    for i in range(3, num+1):
        print(fibolist)
        total = fibolist[i-1] + fibolist[i-2]
        fibolist.append(total)
    return total


print( "fibonaci 10 ->", fibonaci(10))
#recursive concept
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(1, 2):
    print(n, "->", fib(n))