N = input("enter N value: ")
M = input("enter M value: ")
N = int(N)
M = int(M) #467?

while N <= M:
                  
    first_digit = N % 10
    second_digit = (N // 10) % 10
    third_digit = (N // 100) % 10
    fourth_digit = (N // 1000) % 10
    sum_digits = first_digit + second_digit + third_digit + fourth_digit
    print("Sum of digits of " + str(N) + "= " + str(sum_digits)) 
    N = N + 1

#while M >=N:
    #last = M % 10
    #least = (M // 10) % 10
    #first = (M // 100) % 10
    #fourth = (M // 1000) % 10
    #sum_digits = last + least + first + fourth
    #print("Sum of digits of " + str(M) + "= " + str(sum_digits))
    #M= M - 1
