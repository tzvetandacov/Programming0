a = input("Enter a:")
a = int(a)
b = input("Enter b:")
b = int(b)

x = input("Enter x:")
x = int(x)

if x < a:
    print(x, "is lower than lower bound of the interval",a,", ",b)
elif x > b:
    print(x, "is greater than the upper bound of the interval",a ,", ",b)
elif x == a:
    print(x, "is equal to the lower bound of the interval",a,", ",b)
elif x == b:
    print(x, "is equal to the upper bound of the interval",a,", ",b)
else:
    print(x, "is in the interval",a,", ",b)
