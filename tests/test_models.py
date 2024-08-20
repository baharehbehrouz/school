import unittest
from app.models import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Ali", "Ahmadi", "001", "10th", "Mr. Smith")
        self.assertEqual(student.first_name, "Ali")
        self.assertEqual(student.last_name, "Ahmadi")

if __name__ == '__main__':
    unittest.main()
