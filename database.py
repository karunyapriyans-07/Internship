import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    mark INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
""")

cursor.execute("""
INSERT OR IGNORE INTO departments (id, department_name)
VALUES (?, ?)
""", (1, "IT"))

cursor.execute("""
INSERT OR IGNORE INTO departments (id, department_name)
VALUES (?, ?)
""", (2, "IT"))

cursor.execute("""
INSERT OR IGNORE INTO departments (id, department_name)
VALUES (?, ?)
""", (3, "AIDS"))


cursor.execute("""
INSERT OR IGNORE INTO students (id, name, department_id, mark)
VALUES (?, ?, ?, ?)
""", (1, "Karunya", 1, 85))

cursor.execute("""
INSERT OR IGNORE INTO students (id, name, department_id, mark)
VALUES (?, ?, ?, ?)
""", (2, "Gautam", 2, 92))

cursor.execute("""
INSERT OR IGNORE INTO students (id, name, department_id, mark)
VALUES (?, ?, ?, ?)
""", (3, "Ravi", 1, 78))


connection.commit()

print("\n--- DATA INSERTED ---")

print("\n--- ALL STUDENTS ---")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

print("\n--- STUDENTS WITH DEPARTMENT ---")

cursor.execute("""
SELECT students.id,
       students.name,
       departments.department_name,
       students.mark
FROM students
JOIN departments
ON students.department_id = departments.id
""")

results = cursor.fetchall()

for student in results:
    print(student)

cursor.execute("""
UPDATE students
SET mark = ?
WHERE id = ?
""", (90, 1))

connection.commit()

print("\n--- AFTER UPDATE ---")

cursor.execute("""
SELECT * FROM students
""")

students = cursor.fetchall()

for student in students:
    print(student)

cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (3,))

connection.commit()

print("\n--- AFTER DELETE ---")

cursor.execute("""
SELECT * FROM students
""")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()

print("\nDatabase operations completed successfully!")