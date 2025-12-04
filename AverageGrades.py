import StudentGrades

def AverageGrades():
    students = StudentGrades.students
    
    name = input("Student name: ")
    
    if name in students:
        grades = students[name]
        if len(grades) > 0:
            average = sum(grades) / len(grades)
            print(f"Average of {name}: {average:.2f}")
        else:
            print(f"{name} has no grades yet!")
    else:
        print("Student not found..")