def is_prime(num):
    #A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself
    for i in range(2, 10):
        if num % i == 0 and num != i:
            #print(num, " % ", i, " = ")
            return False
    return True

for i in range(2, 21):
	if is_prime(i):
		print("prime = ", i)