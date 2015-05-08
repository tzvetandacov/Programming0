#def n_times_fibonacci(items):
n = input("How many Fibonacci numbers do you want?: ")
n = int(n)
pre_last = 0   
last = 1
total_sum = 0

counter = 0
Fibonacci_list = [pre_last, last]
n_fibonacci = []
while counter < n - 2:
    total_sum = pre_last + last
    Fibonacci_list += [total_sum]
    pre_last = last
    last = total_sum
    counter += 1
print(Fibonacci_list)

#def to_number(digits):
    
