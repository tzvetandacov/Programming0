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
    #n_fibonacci = n_fibonacci + [total_sum]
    pre_last = last
    last = total_sum
    counter += 1
    print(Fibonacci_list)
    #return total_sum
#print(Fibonacci_list)
sum_Fibonacci = 0
# Sum of Fibonacci list:
for number in Fibonacci_list:
    sum_Fibonacci += number

#print(sum_Fibonacci)
# Multiple of Fibonacci list:
multiple_Fibonacci = 1
index = 1
while index <= n + 1:
    multiple_Fibonacci = multiple_Fibonacci * Fibonacci_list[index]
    index +=1
#print(multiple_Fibonacci)
# Reverse sum_Fibonacci number: 42
reverse_list = []
while sum_Fibonacci != 0:
    last_digit = sum_Fibonacci % 10
    reverse_list = [last_digit] + reverse_list
    sum_Fibonacci // 10
#print(reverse_list)
reverse = 0
for digit in reverse_list:
    reverse = reverse * 10 + digit
#print(reverse)
    
    
    
