#dice = input ("Enter a digit")

#from random import randint

#result = randint (1, 6) + int(1)
#print (result)


from random import randint

n = input ("Enter sides:")

n = int (n)              # This can be done as shown below

result1 = randint(1, n)   # Option: result = randint (1, int(n))

result2 = randint (1, n)
print (result1 + result2)
