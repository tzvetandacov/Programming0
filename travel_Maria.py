def travel(travels):
    total_sum = 0

    for travel in travels:
        if travel >=23:
            total_sum = total_sum + 23
        else:
            total_sum = total_sum + travel

        if total_sum >= 50:
            return 50
    return total_sum
print(travel([23, 24, 2]) == 48)
