n = input("n:")
n = int(n)
m = input("m:")
m = int(m)

if n > m:
    greater = n
    lower = m
else:
    lower = n
    greater = m
numbers = range(lower, greater + 1)
for number in numbers:
    if number % 2 ==0:
        print(number, "is even")
    else:
        print(number, "is odd")
