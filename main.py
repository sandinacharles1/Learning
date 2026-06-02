from student_service import StudentService

service = StudentService()

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = float(input("Enter Grade: "))
        service.add_student(student_id, name, age, grade)

    elif choice == "2":
        students = service.get_students()
        if not students:
            print("No students found.")
        else:
            print("ID , Name , Age , Grade")
            for s in students:
                print(f"{s.student_id} , {s.name} , {s.age} , {s.grade}")

    elif choice == "3":
        student_id = int(input("Enter Student ID to delete: "))
        service.delete_student(student_id)

    elif choice == "4":
        break

    else:
        print("Invalid choice. Try again.")