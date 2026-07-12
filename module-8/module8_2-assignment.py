# Name: Natalia Carbajal
# Date: 7/12/2026
# Assignment: Module 8.2
# Purpose: Read student information from a JSON file, add a new student,
# display the original and updated lists, and save the changes.

import json

# Open the JSON file and load the student data into a list
with open("Student.json", "r") as file:
    students = json.load(file)

# Function to print each student's information
def print_students(student_list):
    for student in student_list:
        print(
            f"Name: {student['F_Name']} {student['L_Name']} | "
            f"ID: {student['Student_ID']} | "
            f"Email: {student['Email']}"
        )

# Display the original list of students
print("Original Student List:")
print_students(students)

# Add a new student to the list
students.append(
    {
        "F_Name": "Natalia",
        "L_Name": "Carbajal",
        "Student_ID": 12345,
        "Email": "ncarbajal@email.com"
    }
)

# Display the updated student list
print("\nUpdated Student List:")
print_students(students)

# Save the updated list back to the JSON file
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

# Notify the user that the file has been updated
print("\nStudent.json has been updated.")