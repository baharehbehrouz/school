def display_menu():
    print("Student Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Save and Exit")
    return input("Choose an option: ")

def get_student_details():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")
    teacher = input("Enter teacher's name: ")
    return first_name, last_name, student_id, grade, teacher

def display_students(students):
    print("List of Students:")
    for student in students:
        print(f"{student.first_name} {student.last_name}, ID: {student.student_id}, Grade: {student.grade}, Teacher: {student.teacher}")
