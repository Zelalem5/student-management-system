Student Management System

A Python-based Student Management System designed to manage student information, subjects, marks, grades, and academic performance.

This project was created as part of my Python programming portfolio and demonstrates practical use of Object-Oriented Programming, functions, error handling, JSON file storage, and menu-driven applications.

Features

Student Management

- Add a new student
- View all students
- Search for a student by ID
- Update student information
- Delete a student

Student Marks

- Add marks for subjects
- View student marks
- Calculate total marks
- Calculate average marks
- Determine student grade
- Determine pass/fail status

Data Management

- Save student information to a JSON file
- Load student information from a JSON file
- Handle invalid JSON data
- Preserve student marks when the program is restarted

Input Validation

The program validates:

- Student ID
- Student name
- Student age
- Gender
- Subject names
- Marks
- Numeric input

Invalid input is handled using "try/except" and validation loops.

Grading System

The system uses the following grading system:

Average| Grade
90–100| A
80–89| B
70–79| C
60–69| D
Below 60| F

The system also determines whether the student has passed or failed.

Technologies Used

- Python 3
- Object-Oriented Programming
- Classes and Objects
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- JSON
- File Handling

Example

A student can have marks such as:

===== STUDENT MARKS =====

Student ID : 101
Name       : John

Mathematics     85.00
Physics         78.00
English         92.00

Total           255.00
Average          85.00
Grade                B
Result            PASS

Project Structure

student-management-system/
│
├── student_management.py
├── students.json
├── README.md
└── .gitignore

How to Run

Make sure Python 3 is installed.

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

cd student-management-system

Run the program:

python student_management.py

On Android with Pydroid 3, open "student_management.py" and press the Run button.

What I Learned

Through this project I practiced:

1. Creating classes and objects
2. Creating and using functions
3. Working with lists and dictionaries
4. Validating user input
5. Handling exceptions with "try/except"
6. Working with JSON files
7. Saving and loading application data
8. Building menu-driven applications
9. Calculating student performance
10. Organizing a larger Python project

Future Improvements

Possible future versions could include:

- Login system
- Teacher and administrator accounts
- SQLite database
- Graphical User Interface
- Student report generation
- PDF report cards
- Attendance management
- Course management
- Web-based version
- REST API

Author

Zelalem

Python Developer in Progress

This project is part of my programming portfolio as I continue developing practical software projects for freelance opportunities.