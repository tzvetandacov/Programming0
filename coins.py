def calculate_coins(total_sum):
    dictionary = {"1": 0,
                  "2": 0,
                  "5": 0,
                  "10": 0,
                  "20": 0,
                  "50": 0,
                  "100": 0}
  # total_sum = 4.56

    
    while total_sum >= 1:
        total_sum -= 1
        dictionary["100"] += 1

    while 1 > total_sum  >= 0.5:
        total_sum -= 0.5
        dictionary["50"] += 1
        
    while 0.5 > total_sum >= 0.2:
        total_sum -= 0.2
        dictionary["20"] += 1
        
    while 0.2 > total_sum >= 0.1:
        total_sum -= 0.1
        dictionary["10"] += 1
        
    while 0.1 > total_sum  >= 0.05:
        total_sum -= 0.05
        dictionary["5"] += 1
        
    while 0.05 > total_sum  >= 0.02:
        total_sum -= 0.02
        dictionary["2"] += 1
        
    while 0.02 > total_sum >= 0.01:
        total_sum -= 0.01
        dictionary["1"] += 1
            

    return dictionary

total_sum = input("Enter sum to optimise it for minimum coins: ")
total_sum = float(total_sum)
print(calculate_coins(total_sum))
