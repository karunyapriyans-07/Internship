import csv


def read_student_marks():

    try:
        with open("students.csv", "r") as file:

            reader = csv.DictReader(file)

            students = []

            for row in reader:

                python = float(row["Python"])
                java = float(row["Java"])
                math = float(row["Math"])

                average = (python + java + math) / 3

                student = {
                    "name": row["Name"],
                    "average": average
                }

                students.append(student)

            if not students:
                print("No student records found.")
                return

            print("\n--- STUDENT MARKS ---")

            for student in students:
                print(
                    student["name"],
                    "- Average:",
                    round(student["average"], 2)
                )

            topper = max(students, key=lambda student: student["average"])

            total_average = sum(
                student["average"] for student in students
            )

            class_average = total_average / len(students)

            print("\nTopper:", topper["name"])
            print("Topper Average:", round(topper["average"], 2))

            print(
                "Class Average:",
                round(class_average, 2)
            )

    except FileNotFoundError:
        print("Error: students.csv was not found.")

    except ValueError:
        print("Error: Marks must contain valid numbers.")

    except KeyError:
        print("Error: CSV file is missing a required column.")


read_student_marks()