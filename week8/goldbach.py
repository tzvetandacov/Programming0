def is_prime(number):
    devisor = 2
    while devisor < number:
        if number % devisor == 0:
            return False
        devisor += 1
    return True

def goldbach(n):
    result = []
    middle = n / 2
    if n % 2 !=0 or n <= 2:
        return False
    x = 3
    while x <= middle:
        y = n - x
        if is_prime(x) and is_prime(y):
            result.append((x, y))
        x += 1 
    return result
print(goldbach(100))

