
from database import connect_db, create_tables
from course import add_course, view_courses
from student import (
    add_student,
    view_students,
    search_student,
    search_student_by_id,
    update_student,
    delete_student
)


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a positive number")

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Input cannot be empty")


def show_menu():
    print("\n===== COLLEGE COURSE MANAGER =====")
    print("1. Add Course")
    print("2. View Courses")
    print("3. Add Student")
    print("4. View Students")
    print("5. Search Student by Name")
    print("6. Search Student by ID")
    print("7. Update Enrollment")
    print("8. Delete Student")
    print("9. Exit")


conn = None

try:
    conn = connect_db("demo_college.db")
    create_tables(conn)
    print("Database initialized successfully!")

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            course_id = get_integer("Enter course ID: ")
            course_name = get_non_empty_string("Enter course name: ")

            add_course(conn, course_id, course_name)

        elif choice == "2":
            view_courses(conn)

        elif choice == "3":
            name = get_non_empty_string("Enter student name: ")
            course_id = get_integer("Enter course ID: ")

            add_student(conn, name, course_id)

        elif choice == "4":
            view_students(conn)

        elif choice == "5":
            name = get_non_empty_string("Enter student name: ")

            search_student(conn, name)

        elif choice == "6":
            student_id = get_integer("Enter student ID: ")

            search_student_by_id(conn, student_id)

        elif choice == "7":
            student_id = get_integer("Enter student ID: ")
            course_id = get_integer("Enter course ID: ")

            update_student(conn, student_id, course_id)

        elif choice == "8":
            student_id = get_integer("Enter student ID: ")

            while True:
                ch = input("Are you sure? (y/n): ").strip().lower()

                if ch == "y":
                    delete_student(conn, student_id)
                    break

        elif choice == "9":
            print("Thank you for using College Course Manager!")
            break

        else:
            print("Invalid choice! Please select 1-9.")
            
finally:
    if conn is not None:
        conn.close()
