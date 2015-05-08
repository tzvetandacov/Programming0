n = input("enter value for n:")
m = input("enter value for m:")
n = int(n)    # 13
m = int(m)    # 27

if (n % 10) < (m % 10):
    print(m)
elif (n % 10) > (m % 10):
    print(n)
elif (n % 10) == (m % 10):

    if n > m:
        print(n)
    if m > n:
        print(m)
    if n == m:
        print("digits are even")
      
