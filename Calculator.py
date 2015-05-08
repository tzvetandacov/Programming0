a = input ("Enter value for a:")
a = int(a)
b = input ("Enter value for b:")
b = int(b)
oper = input("Enter operation:")
result = False

if oper == "+":
    result = a + b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a * b
elif oper == "/":
    result = a / b
elif oper == "%":
    result = a % b
if result:
    print(result)
else:
    print("We do not support that operation")
