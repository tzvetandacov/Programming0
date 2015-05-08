def reverse_list(items):
    index = len(items) - 1
    reversed_list = []

    while index >= 0: 
        reversed_list = reversed_list + [items[index]]
        index = index - 1

    return reversed_list


def reverse_number(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]
        n = n // 10
    
    result = 0
    for digit in digits:
        result = result * 10 + digit

    return result

def sum_list_to_number(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]
        n = n // 10

        result = 0
    for digit in digits:
        result = result + digit

    return result




def product_list(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]
        n = n // 10

        result = 1
    for digit in digits:
        result = result * digit
        
    return result
    

