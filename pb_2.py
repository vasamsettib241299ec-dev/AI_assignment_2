# Student records stored using dictionaries
students = [
    {"name": "Ravi", "attendance": 90, "assignment": 85, "exam": 80},
    {"name": "Sita", "attendance": 95, "assignment": 92, "exam": 90},
    {"name": "Arun", "attendance": 80, "assignment": 70, "exam": 75},
    {"name": "Priya", "attendance": 88, "assignment": 95, "exam": 98},
    {"name": "Kiran", "attendance": 85, "assignment": 80, "exam": 85}
]

# 1. Calculate each student's average mark
for student in students:
    student["average"] = (
        student["assignment"] + student["exam"]
    ) / 2

# 2. Calculate class average
class_average = sum(
    student["average"] for student in students
) / len(students)

print("Class average:", round(class_average, 2))

# 3. Identify students above class average
print("\nStudents above class average:")

for student in students:
    if student["average"] > class_average:
        print(student["name"], student["average"])

# 4. Sort students by average marks (descending)
students.sort(
    key=lambda student: student["average"],
    reverse=True
)

print("\nStudents sorted by marks:")

for student in students:
    print(student["name"], student["average"])

# 5. Display the top three students
print("\nTop three students:")

for student in students[:3]:
    print(student["name"], student["average"])