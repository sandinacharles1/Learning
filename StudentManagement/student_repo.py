import sqlite3
from student import Student

class StudentRepository:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade REAL
            )
        """)
        self.conn.commit()

    def add_student(self, student):
        self.conn.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student.student_id, student.name, student.age, student.grade)
        )
        self.conn.commit()

    def get_students(self):
        cursor = self.conn.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [Student(r[0], r[1], r[2], r[3]) for r in rows]

    def delete_student(self, student_id):
        self.conn.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.conn.commit()
