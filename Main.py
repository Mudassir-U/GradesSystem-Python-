from StudentGrades import StudentGrades
from AverageGrades import AverageGrades
from RemoveStudent import RemoveStudent
print('Welcome To Grade Central')
while True:
    print(
        "\n[1] - Enter Grades"
        "\n[2] - Remove Student"
        "\n[3] - Student Average Grades"
        "\n[4] - Exit"
    )
    choice = int(input("Enter your Choice: "))
    
    if choice == 1:
        StudentGrades()
    elif choice == 2:
        RemoveStudent()
    elif choice == 3:
        AverageGrades()
    elif choice == 4:
        print("Exiting ....")
        break
    else:
        print("You made the wrong Choice.Try Again.")

        