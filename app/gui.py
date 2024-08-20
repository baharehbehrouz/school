import tkinter as tk
from tkinter import messagebox, ttk
from app.data_manager import DataManager


class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("400x300")
        self.root.configure(bg="#f5f5f5")

        # Load existing students from CSV file
        self.students = DataManager.load_data()

        # Labels and Entries for Student Information
        labels = ["First Name", "Last Name", "Student ID", "Subject", "Teacher"]
        self.entries = {}

        for i, label_text in enumerate(labels):
            label = ttk.Label(root, text=label_text, background="#f5f5f5", font=("Helvetica", 10))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="W")

            entry = ttk.Entry(root, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label_text] = entry

        # Submit Button
        submit_btn = ttk.Button(root, text="Submit", command=self.submit)
        submit_btn.grid(row=5, column=1, pady=10)

        # Button to show the list of students
        show_btn = ttk.Button(root, text="Show Students", command=self.show_students)
        show_btn.grid(row=6, column=1)

    def submit(self):
        # Get the values from the entries
        student_data = {key: entry.get() for key, entry in self.entries.items()}

        # ذخیره اطلاعات دانش‌آموز در لیست
        self.students.append(student_data)

        # Save students to CSV file
        DataManager.save_data(self.students)

        # Show a message box with the entered data
        messagebox.showinfo("Student Info",
                            f"Student {student_data['First Name']} {student_data['Last Name']} with ID {student_data['Student ID']} registered for {student_data['Subject']} with teacher {student_data['Teacher']}.")

        # Clear the entries after submission
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def show_students(self):
        # نمایش لیست دانش‌آموزان در یک پنجره جدید
        students_info = "\n".join(
            [f"{s['First Name']} {s['Last Name']} - {s['Student ID']} ({s['Subject']}, {s['Teacher']})" for s in
             self.students])
        messagebox.showinfo("Student List", students_info if students_info else "No students registered yet.")
