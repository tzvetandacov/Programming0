n = input("Enter n: ")
n = int(n)

def factorial(n):

    start = 1
    factorial = 1

    while start <= n:
        factorial = start * factorial
        start += 1
    return factorial
print(factorial(n))
    
