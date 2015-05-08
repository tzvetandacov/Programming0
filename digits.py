n = input("Enter four digits number: ")
n = int(n)

digits = []
start = 1
while n !=0:
    digit = n % 10
    digits = [digit] + digits
    n = n //10
print(digits)

#for digit in digits:
 #   total_sum = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
#print(total_sum)

n = 0

for digit in digits:
    n = n * 10 + digit
    print(n)
print(n)
    

