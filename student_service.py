from student import Student
from student_repo import StudentRepository

class StudentService:
    def __init__(self):
        self.repo = StudentRepository()

    def add_student(self, student_id, name, age, grade):
        if age <= 15:
            print("Invalid since age must be greater than 15.")
            return
        if grade <= 70:
            print("Invalid since grade must be greater than 70.")
            return
        new_student = Student(student_id, name, age, grade)
        self.repo.add_student(new_student)
        print("Student added!")

    def get_students(self):
        return self.repo.get_students()

    def delete_student(self, student_id):
        self.repo.delete_student(student_id)
        print("Student deleted!")