# Grade Central - Student Grade Management System

A simple command-line application for managing student grades, built with Python. This project allows teachers or administrators to add grades, remove students, and calculate average grades for students.

## 📋 Features

- **Add Student Grades**: Enter grades for students (supports multiple grades per student)
- **Remove Students**: Delete a student and all their grades from the system
- **Calculate Averages**: Get the average grade for any student
- **Interactive Menu**: User-friendly command-line interface with numbered options
- **Persistent Session**: Grades are stored in memory during the session

## 🚀 Requirements

- Python 3.x (Python 3.6 or higher recommended)
- No external dependencies required (uses only Python standard library)

## 📦 Installation

1. Clone or download this repository
2. Ensure Python is installed on your system
3. Navigate to the project directory

```bash
cd "D:\PRACTICE\Python course project"
```

## 💻 Usage

Run the main program:

```bash
python Main.py
```

### Menu Options

Once the program starts, you'll see the following menu:

```
Welcome To Grade Central

[1] - Enter Grades
[2] - Remove Student
[3] - Student Average Grades
[4] - Exit
```

### Option 1: Enter Grades
- Prompts for student name and grade
- If the student already exists, adds the new grade to their existing grades
- If the student is new, creates a new entry with the grade
- Displays the updated student dictionary

**Example:**
```
Enter your Choice: 1
Student name: John Doe
Grade: 85
Adding....
Successfully Added..
{'John Doe': [85]}
```

### Option 2: Remove Student
- Prompts for student name
- Removes the student and all their grades from the system
- Shows an error message if the student is not found
- Displays the updated student dictionary

**Example:**
```
Enter your Choice: 2
Student name: John Doe
Student John Doe removed successfully!
{}
```

### Option 3: Student Average Grades
- Prompts for student name
- Calculates and displays the average of all grades for that student
- Shows an error message if the student is not found
- Handles cases where a student has no grades

**Example:**
```
Enter your Choice: 3
Student name: John Doe
Average of John Doe: 87.50
```

### Option 4: Exit
- Safely exits the program
- Displays "Exiting ...." message

## 📁 Project Structure

```
Python course project/
│
├── Main.py              # Main entry point with menu system
├── StudentGrades.py     # Module for adding student grades
├── RemoveStudent.py     # Module for removing students
├── AverageGrades.py     # Module for calculating grade averages
├── README.md           # This file
└── __pycache__/        # Python cache directory (auto-generated)
```


## 📝 Example Workflow

1. **Start the program**: `python Main.py`
2. **Add grades for multiple students**:
   - Choose option 1, enter "Alice", grade 90
   - Choose option 1, enter "Bob", grade 85
   - Choose option 1, enter "Alice", grade 95 (adds second grade to Alice)
3. **View averages**:
   - Choose option 3, enter "Alice" → Shows average: 92.50
   - Choose option 3, enter "Bob" → Shows average: 85.00
4. **Remove a student**:
   - Choose option 2, enter "Bob" → Removes Bob and all his grades
5. **Exit**: Choose option 4


**Happy Grading! 📚✨**

