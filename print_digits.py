whole_digit = input("enter digit: ")
whole_digit = int(whole_digit)

# 1356


while whole_digit > 0:
    
    last_digit = whole_digit % 10
    print(last_digit)
    whole_digit = whole_digit // 10
