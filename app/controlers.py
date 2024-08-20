import pandas as pd
from app.models import Student

class StudentController:
    def __init__(self):
        self.students = []

    def save_and_exit(self):
        data = [student.to_dict() for student in self.students]
        df = pd.DataFrame(data)
        df.to_excel('data/students.xlsx', index=False, engine='xlsxwriter')
