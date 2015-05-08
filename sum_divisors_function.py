def divisors():
    n = input("enter number: ")
    n = int(n)
    divisors = []
    counter = 1
    while counter < n:
        if n % counter == 0:
            divisors += [counter]
            counter += 1
        else:
            counter += 1
    return divisors
print(divisors())

def sum_divisors():
    total_sum = 0
    
    for divisor in divisors():
        total_sum = divisor + total_sum
    
    return total_sum
print(sum_divisors())
