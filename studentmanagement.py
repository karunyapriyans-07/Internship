class Student:
    def __init__(self, roll_no, name, department):
        self.roll_no = roll_no
        self.name = name
        self.department = department

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Department:", self.department)
        print("-----------------------")


students = []


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")

    student = Student(roll_no, name, department)
    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students available.")
    else:
        print("\n--- STUDENT LIST ----")

        for student in students:
            student.display()


def search_student():
    roll_no = input("Enter roll number to search: ")

    found = False

    for student in students:
        if student.roll_no == roll_no:
            print("\nStudent found!")
            student.display()
            found = True
            break

    if not found:
        print("\nStudent not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


while True:

    print("\n--- STUDENT MANAGEMENT SYSTEM ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")