n = input("enter long digit: ")
n = int(n)

sum = 0
#259


while n > 0:
    last_digit= n % 10
    sum = last_digit + sum
    n = n // 10

print(sum)

