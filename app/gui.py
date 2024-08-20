import tkinter as tk
from tkinter import messagebox
from app.data_manager import DataManager

class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")

        # Load existing students from CSV file
        self.students = DataManager.load_data()

        # Labels and Entries for Student Information
        tk.Label(root, text="First Name").grid(row=0, column=0)
        tk.Label(root, text="Last Name").grid(row=1, column=0)
        tk.Label(root, text="Student ID").grid(row=2, column=0)
        tk.Label(root, text="Subject").grid(row=3, column=0)
        tk.Label(root, text="Teacher").grid(row=4, column=0)

        self.first_name = tk.Entry(root)
        self.last_name = tk.Entry(root)
        self.student_id = tk.Entry(root)
        self.subject = tk.Entry(root)
        self.teacher = tk.Entry(root)

        self.first_name.grid(row=0, column=1)
        self.last_name.grid(row=1, column=1)
        self.student_id.grid(row=2, column=1)
        self.subject.grid(row=3, column=1)
        self.teacher.grid(row=4, column=1)

        # Submit Button
        tk.Button(root, text="Submit", command=self.submit).grid(row=5, column=1)

        # Button to show the list of students
        tk.Button(root, text="Show Students", command=self.show_students).grid(row=6, column=1)

    def submit(self):
        # Get the values from the entries
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        student_id = self.student_id.get()
        subject = self.subject.get()
        teacher = self.teacher.get()

        # ذخیره اطلاعات دانش‌آموز در لیست
        student = {
            "First Name": first_name,
            "Last Name": last_name,
            "Student ID": student_id,
            "Subject": subject,
            "Teacher": teacher
        }
        self.students.append(student)

        # Save students to CSV file
        DataManager.save_data(self.students)

        # Show a message box with the entered data
        messagebox.showinfo("Student Info", f"Student {first_name} {last_name} with ID {student_id} registered for {subject} with teacher {teacher}.")

        # Clear the entries after submission
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.student_id.delete(0, tk.END)
        self.subject.delete(0, tk.END)
        self.teacher.delete(0, tk.END)

    def show_students(self):
        # نمایش لیست دانش‌آموزان در یک پنجره جدید
        students_info = "\n".join([f"{s['First Name']} {s['Last Name']} - {s['Student ID']} ({s['Subject']}, {s['Teacher']})" for s in self.students])
        messagebox.showinfo("Student List", students_info if students_info else "No students registered yet.")
