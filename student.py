
import sqlite3


def add_student(conn, name, course_id):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT course_id
            FROM courses
            WHERE course_id = ?
        """, (course_id,))

        course = cursor.fetchone()

        if not course:
            print("Course does not exist.")
            return

        cursor.execute("""
            INSERT INTO students (name, course_id)
            VALUES (?, ?)
        """, (name, course_id))

        conn.commit()
        print("Student details added successfully!")

    except sqlite3.IntegrityError:
        conn.rollback()
        print("Could not add student due to a database constraint.")


def view_students(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.id, students.name, courses.course_name
        FROM students
        INNER JOIN courses
        ON courses.course_id = students.course_id
    """)

    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"ID: {student[0]} || "
                f"Name: {student[1]} || "
                f"Course: {student[2]}"
            )
    else:
        print("No students enrolled yet.")


def search_student(conn, name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.id, students.name, courses.course_name
        FROM students
        INNER JOIN courses
        ON courses.course_id = students.course_id
        WHERE students.name = ?
    """, (name,))

    students = cursor.fetchall()

    if students:
        for student in students:
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Course: {student[2]}")
            print("-------------")
    else:
        print("Student not found.")


def search_student_by_id(conn, student_id):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.id, students.name, courses.course_name
        FROM students
        INNER JOIN courses
        ON courses.course_id = students.course_id
        WHERE students.id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if student:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Course: {student[2]}")
    else:
        print("Student not found.")


def update_student(conn, student_id, course_id):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT course_id
            FROM courses
            WHERE course_id = ?
        """, (course_id,))

        course = cursor.fetchone()

        if not course:
            print("Course does not exist.")
            return

        cursor.execute("""
            UPDATE students
            SET course_id = ?
            WHERE id = ?
        """, (course_id, student_id))

        if cursor.rowcount > 0:
            conn.commit()
            print("Student details updated successfully!")
        else:
            print("Student not found.")

    except sqlite3.IntegrityError:
        conn.rollback()
        print("Invalid course ID.")


def delete_student(conn, student_id):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))

    if cursor.rowcount > 0:
        conn.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")
