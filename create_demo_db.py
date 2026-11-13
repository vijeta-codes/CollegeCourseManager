
from database import connect_db, create_tables

conn = connect_db("demo_college.db")

create_tables(conn)

courses = [
    (101, "Python"),
    (102, "Java"),
    (103, "SQL"),
    (104, "Django"),
    (105, "Flask")
]

conn.executemany("""
    INSERT OR IGNORE INTO courses (course_id, course_name)
    VALUES (?, ?)
""", courses)

students = [
    ("Alex", 101),
    ("Emma", 102),
    ("Noah", 103),
    ("Sophia", 104),
    ("Liam", 105)
]

conn.executemany("""
    INSERT INTO students (name, course_id)
    VALUES (?, ?)
""", students)

conn.commit()
conn.close()

print("Demo database created successfully!")
