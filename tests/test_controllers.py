import unittest
from app.controllers import StudentController

class TestStudentController(unittest.TestCase):
    def test_add_student(self):
        controller = StudentController()
        initial_count = len(controller.students)
        controller.add_student()
        self.assertEqual(len(controller.students), initial_count + 1)

if __name__ == '__main__':
    unittest.main()
