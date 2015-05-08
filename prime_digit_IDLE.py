n = input("please enter 4 digit number: ")
n = int(n) # 1356
digit_list = []
start = 2
is_prime = True
while n > 0:
    digit = n % 10
    digit_list = [digit] + digit_list
    n = n // 10
print(digit_list)    
print(digit_list[0])
while True:
    while start < digit_list[0]:
        if digit_list[0] % start ==0:
            is_prime = False
            print("first is not prime")
        else:
            print(digit, "first is a prime")
        start += 1
    while start < digit_list[1]:
        if digit_list[1] % start ==0:
            is_prime = False
            print("second is not prime")
        else:
            print("second is a prime")
        start += ArithmeticError
    while start < digit_list[2]:
        if digit_list[2] % start ==0:
            is_prime = False
            print("third is not prime")
        else:
            print("third is a prime")
        start += 1
    while start < digit_list[3]:
        if digit_list[3] % start ==0:
            is_prime = False
            print("fourth is not prime")
        else:
            print("fourth is a prime")
        start += 1
        

                   
            
