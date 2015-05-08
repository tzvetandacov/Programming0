from random import randint
def n_random_numbers(n, lowest, highest):
    start = 1
    result = []
    
    while start < n:
        next_number = randint(lowest, highest)
        result = result + [next_number]
        start += 1
    return result

