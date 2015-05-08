def factorial(n):
    result = 1
    while n >= 2:
        result = n * result
        n -= 1
    return result


def number_to_digits(n):
    result = []
    while n != 0:
        result = [n % 10] + result
        n = n // 10
    return result


def fact_digits(n):
    digits = number_to_digits(n)
    result = 0
    for digit in digits:
        result += factorial(digit)
    return result


print(fact_digits(44))