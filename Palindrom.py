x = input("Enter x: ")
x = int(x)

# 4793

a = x // 1000
b = (x // 100) % 10
c = (x // 10) % 10
d = (x % 10)

if a == d and b == c:
    print("The number is Palindrom")

else:
    print("The number is not Palindrom")



