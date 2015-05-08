import time

today = time.strftime("%A")

print(today)
if today == "Sunday":
    print("It is Sunday, not Friday ;( ")
elif today == "Friday":
    print("It is Friday ;) ")
