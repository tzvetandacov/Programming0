def is_credit_card_valid(number):
    if len(number) % 2 == 0:
        return False
    to_list = []
    to_str = ""
    result = 0
    for index in range(0, len(number)):
        if index % 2 == 0:
            to_list += [number[index]]
        else:
            to_list += [int(number[index]) * 2]

    for member in to_list:
        to_str += str(member)
    for member in to_str:
        result += int(member)
    if result % 10 == 0:
        return True
    else:
        return False
print(is_credit_card_valid("79927398713"))