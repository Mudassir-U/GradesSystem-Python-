students = {}

def StudentGrades():
    name = input("Student name: ")
    grade = int(input("Grade: "))

    print('Adding....')
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]
    print('Successfully Added..')
    print(students)

