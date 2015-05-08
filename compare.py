x = input ("X:")
y = input ("Y:")
x = int(x)
y = int(y)

if x > y:
    print(x, "is bigger than", y)
elif x < y:
    print(y, "is bigger than", x)
else:
    print(x, "is equal to", y)
