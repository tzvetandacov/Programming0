def count_digits_in_number(x):
    digits = 0
    
    while x != 0:
        x = x // 10
        digits += 1
    return digits
        
