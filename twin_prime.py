p = input("Enter 1 digit: ")
p = int(p)
twin_prime_up = p + 2
twin_prime_down = p - 2
is_prime = True

start = 2

if p == 1:
    is_prime=False
    print("1 is not prime number")
  
while start < p:
    if p % start ==0:
        is_prime = False
        print("The number is no prime")
        break
    start = start + 1
while start < twin_prime_up:
    if twin_prime_up % start ==0:
        twin_prime_up = False
    
    start = start + 1
while start < twin_prime_down:
    if twin_prime_down % start ==0:
        twin_prime_down = False
        
        break
    start = start + 1
if twin_prime_down !=1:
    
    if is_prime and twin_prime_up and twin_prime_down:
        print("The number", p, "has twin prime up: ", twin_prime_up, "and twin prime down: ", twin_prime_down)
    elif is_prime and twin_prime_up:
        print("The number", p, "has twin prime up: ", twin_prime_up)
    elif is_prime and twin_prime_down:
        print("The number", p, "has twin prime down: ", twin_prime_down)
else:
    if is_prime and twin_prime_up:
        print("The number", p, "has twin prime up: ", twin_prime_up)
    
   
