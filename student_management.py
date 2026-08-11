import json
class Student:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = {}

    def display(self):
        print("-" * 40)
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Marks      :", self.marks)


students = []

#=========== Add Student ============
def add_student():
# Student ID
 sid = input("Enter student ID: ").strip()

# Student Name
 while True:
    name = input("Enter student Name: ").strip()

    if name == "":
        print("Name cannot be empty.")

    elif not name.replace(" ", "").isalpha():
        print("Name must contain letters only.")

    else:
        break

# Student Age
 while True:
    try:
        age = int(input("Enter student Age: "))

        if age < 5 or age > 100:
            print("Please enter a valid age between 5 and 100.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a number for age.")

# Student Gender
 while True:
    gender = input("Enter student Gender: ").strip()

    if gender == "":
        print("Gender cannot be empty.")

    elif not gender.replace(" ", "").isalpha():
        print("Gender must contain letters only.")

    else:
        break

# Create student object
 student1 = Student(sid, name, age, gender)
 students.append(student1)
 print("Student added successfully!")
  
#============ View All Student =========
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== ALL STUDENTS =====")

    for student in students:
        student.display()
        
        
#============ Search Student =========
def search_student():
    search_id = input("Enter student ID to search: ").strip()

    found = False

    for student in students:
        if student.student_id == search_id:
            print("Student found!")
            student.display()
            found = True
            break

    if found == False:
        print("Student not found.")

#=========== Update Student ========
def update_student():
    search_id = input("Enter student ID to update: ").strip()

    found = False

    for student in students:

        if student.student_id == search_id:

            print("\nStudent found!")
            student.display()

            # Update Name
            while True:
                name = input("Enter new name: ").strip()

                if name == "":
                    print("Name cannot be empty.")

                elif not name.replace(" ", "").isalpha():
                    print("Name must contain letters only.")

                else:
                    student.name = name
                    break

            # Update Age
            while True:
                try:
                    age = int(input("Enter new age: "))

                    if age < 5 or age > 100:
                        print("Please enter a valid age between 5 and 100.")
                        continue

                    student.age = age
                    break

                except ValueError:
                    print("Invalid input. Please enter a number for age.")

            # Update Gender
            while True:
                gender = input("Enter new gender: ").strip()

                if gender == "":
                    print("Gender cannot be empty.")

                elif not gender.replace(" ", "").isalpha():
                    print("Gender must contain letters only.")

                else:
                    student.gender = gender
                    break

            print("\nStudent updated successfully!")

            student.display()

            found = True
            break

    if not found:
        print("Student not found.")   
        
#============ Delete Student =======

def delete_student():
    search_id = input("Enter student ID to delete: ").strip()

    found = False

    for student in students:
        if student.student_id == search_id:
            students.remove(student)
            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")   
  
  
 #============ Add Mark ============

def add_mark():
    search_id = input("Enter student ID: ").strip()

    found = False

    for student in students:
        if student.student_id == search_id:
            print("Student found!")
            student.display()

            subject = input("Enter subject: ").strip()

            # Check subject name
            if subject == "":
                print("Subject cannot be empty.")
                return

            # Check if subject already exists
            if subject in student.marks:
                print("This subject already has a mark.")
                return

            # Get mark
            while True:
                try:
                    mark = float(input("Enter mark (0-100): "))

                    if mark < 0 or mark > 100:
                        print("Mark must be between 0 and 100.")
                        continue

                    break

                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Save mark
            student.marks[subject] = mark

            print("Mark added successfully!")
            return

    print("Student not found.")    
    
#========= View student mark =====

def view_student_marks():
    search_id = input("Enter student ID: ").strip()

    for student in students:
        if student.student_id == search_id:

            print("\n===== STUDENT MARKS =====")
            print("Student ID :", student.student_id)
            print("Name       :", student.name)

            if len(student.marks) == 0:
                print("No marks found.")
                return

            print("\nSubject       Mark")
            print("-" * 25)

            for subject, mark in student.marks.items():
                print(f"{subject:<15} {mark:.2f}")

            return

    print("Student not found.")
    
#====== Student Result =======
def student_result():
    search_id = input("Enter student ID: ").strip()

    found = False

    for student in students:
        if student.student_id == search_id:
            found = True

            if len(student.marks) == 0:
                print("No marks found for this student.")
                return

            total = sum(student.marks.values())
            average = total / len(student.marks)

            # Determine grade
            if average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            # Determine pass/fail
            if average >= 50:
                result = "PASS"
            else:
                result = "FAIL"

            print("\n===== STUDENT RESULT =====")
            print("Student ID :", student.student_id)
            print("Name       :", student.name)
            print("-" * 40)

            for subject, mark in student.marks.items():
                print(f"{subject:<15} {mark:.2f}")

            print("-" * 40)
            print(f"Total      : {total:.2f}")
            print(f"Average    : {average:.2f}")
            print(f"Grade      : {grade}")
            print(f"Result     : {result}")

            break

    if not found:
        print("Student not found.")
        
        
#========= Save File =============
def save_students():
    data = []

    for student in students:
        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
            "marks": student.marks
        }

        data.append(student_data)

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Students saved successfully!")
    
    
# ========== Load Student =========
def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        students.clear()

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["gender"]
            )

            student.marks = item["marks"]

            students.append(student)

        print("Students loaded successfully!")
        
        for student in students:
           student.display()

    except FileNotFoundError:
        print("No saved student data found.")

    except json.JSONDecodeError:
        print("Error: Student file contains invalid data.")
     
#============== Menu==============
   
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("     1. Add Student")
    print("     2. View All Students")
    print("     3. Search Student")
    print("     4. Update Student")
    print("     5. Delete Student")
    print("     6. Add Mark")
    print("     7. View Student Mark")
    print("     8. Student Result")
    print("     9. Save Student")
    print("     10. Load Student")
    print("     11. Exit")
 

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add student
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        add_mark()
    elif choice == "7":
        view_student_marks()
    elif choice == "8":
        student_result()
    elif choice == "9":
        save_students()
    elif choice == "10":
        load_students()
    elif choice == "11":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")