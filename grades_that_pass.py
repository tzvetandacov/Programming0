def grades_that_pass(students, grades, limit):
    
    result = []
    start = 0
    
    while start < len(students):
        grade = grades[start]
        name = students[start]
        
        if grade >= limit:
            result = result + [name]

        start += 1

    return result
students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

print(grades_that_pass(students, grades, 3))
#print(grades_that_pass(("Mitko", "Sasho", "Georgi", "Alex"], grades, 4)
def grades_that_pass_for(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        name = students[index]

        if grades >= limit:
            result = result + [name]

        index += 1
        
    return result


students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]


print(grades_that_pass(students, grades, 4))
