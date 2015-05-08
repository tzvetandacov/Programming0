n = input("enter number: ")
n = int(n)
increase = start = 6 #28
prime = []
sum_divisors = 0
counter = 1
while True:
    while counter < increase:
        if increase % counter == 0:
            sum_divisors += counter
            counter += 1
        else:
            counter += 1

    if increase == sum_divisors:
        prime = prime + [increase]
        increase += 1
        print(prime)
    else:
        # print(n, "is not perfect")
        increase += 1
        
