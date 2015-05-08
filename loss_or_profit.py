def loss_or_profit(income, outcome):
    result = 0
    income_sum = sum(income)
    outcome_sum = sum(outcome)

    if income_sum < 0 or outcome_sum < 0:
        return "Invalid income or outcome - negative result"
    result = income_sum - outcome_sum

    #return str(result)
    if result > 0:
        return "+" + str(result)
    elif result == 0:
        return "=" + str(result)
    else:
        return str(result)
print(loss_or_profit([100,20], [80,40]))
