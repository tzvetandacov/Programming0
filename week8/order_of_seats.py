def inc(x):
    return x + 1

def order_of_seats(cinema):
    r = 1
    e = 0
    cinematic = [[e,e,e],
                 [r,e,r],
                 [r,e,e],
                 [e,r,r]]
    result = []
    full_row = len(cinema[0])
    for empty_seats in range(1, len(cinema[0])+1):
        for index_row in range(0, len(cinema)):
            for index_col in range(0, len(cinema[0])):
                if sum(cinema[index_row]) == full_row - empty_seats:
                    if cinema[index_row][index_col] == e:
                        result.append(("your_seat_is:",inc(index_row) ,inc(index_col)))
    return result
print(order_of_seats(cinematic))


