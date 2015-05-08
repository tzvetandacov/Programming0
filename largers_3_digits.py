x = a = input("enter 1 digit: ")
y = b = input("enter 1 digit: ")
z = c = input("enter 1 digit: ")
a = int(a)
b = int(b)
c = int(c)
x = int(x)
y = int(y)
z = int(z)

if x < y and y < z: #zyx
    y = y * 10
    z = z * 100
    Sum = x + y + z
    print (Sum)
if y < x and x < z:  #zxy
    z = z * 100
    x = x * 10
    Sum = x + y + z
    print(Sum)

if z < y and y < x:   #xyz
    x = x * 100
    y = y * 10
    Sum = x + y + z
    print(Sum)

if z < x and x < y:   #yxz
    y = y * 100
    x = x * 10
    Sum = x + y + z
    print(Sum)

if y < z and z < x:  #xzy
    x = x * 100
    z = z * 10
    Sum = x + y + z
    print(Sum)

if x < z and z < y:  #yzx
    y = y * 100
    z = z * 10
    Sum = x + y + z
    print(Sum)



if c < b and b < a: #abc
    c = c * 100
    b = b * 10
    Sum = a + b + c
    print(Sum)
if b < c and c < a: #acb
    b = b * 100
    c = c * 10
    Sum = a + b + c
    print(Sum)
if c < a and a < b: #bac
    c = c * 100
    a = a * 10
    Sum = a + b + c
    print(Sum)
if a < c and c < b: #bca
    a = a * 100
    c = c * 10
    Sum = a + b + c
    print(Sum)
if a < b and b < c: #cba
    a = a * 100
    b = b * 10
    Sum = a + b + c
    print(Sum)
if b < a and a < c: #cab
    b = b * 100
    a = a * 10
    Sum = a + b + c
    print(Sum)

