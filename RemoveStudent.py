import StudentGrades

def RemoveStudent():
    students = StudentGrades.students
    
    name = input("Student name: ")
    if name in students:
        del students[name]
        print(f"Student {name} removed successfully!")
    else:
        print('Student Not Found!')
    print(students)