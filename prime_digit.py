n = input("Enter multi digit number: ") # 2467
n = int(n) 
digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10
has_prime_digit = False
    
for digit in digits:
    if digit in [2, 3, 5, 7]:
       has_prime_digit = True
       break

if has_prime_digit:
    print("Yes")
else:
    print("No")
