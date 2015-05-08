# 1. input integer
# 2. empty list
# 3. start counter = 1
# 4. flagva promenliva ( TRUE )
# 5. loop from 1 to n - 1
# 6. if True - add to the list
# 7. print list

n = input("enter number: ")
n = int(n)
divisors = []
counter = 1
while counter < n:
    if n % counter == 0:
        divisors += [counter]
        counter += 1
    else:
        counter +=1
print(divisors)
        
