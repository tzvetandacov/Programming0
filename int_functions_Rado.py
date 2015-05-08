# 123
# 123 -> [1, 2, 3] def to_digits(n)
# [1, 2, 3] -> [3, 2, 1] def reverse_list(items)
#[3, 2, 1] -> 321 def to_number(digits)

def reverse_int(n):
    return to_number(reverse_list(to_digits(n)))


# Drugo reshenie:
# n = 0
# result = 320 + 1 = 321
# digit = 1

def reverse_int2(n):
    result = 0

    while n != 0:
        digit = n% 10
        result = result * 10 + digit
        n = n // 10
    return result
print(reverse_int2(456))
