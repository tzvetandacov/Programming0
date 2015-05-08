x = input("Enter x: ")
x = int(x)

# 479

a = x // 100
b = (x // 10) % 10
c = (x % 10)

y = c * 100
z = b * 10
w = a
Sum = y + z + w
print(Sum)

