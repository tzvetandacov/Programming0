from datetime import datetime

first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
family_name = input("Enter family name: ")
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)



current_age = datetime.today().year - birth_year

person = {"first_name": first_name,
 "second_name": second_name,
 "family_name": family_name,
 "birth_year": birth_year,
 "current_age": current_age}
for key in person:
    value = person[key]
    print(key, value)
