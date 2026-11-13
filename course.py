import sqlite3  

def add_course(conn, course_id, course_name):
  cursor = conn.cursor()
  try:
    cursor.execute("""
     INSERT INTO courses(course_id, course_name)
     VALUES(?, ?)
    """,(course_id, course_name))
    conn.commit()
    print("Course added successfully")
  except sqlite3.IntegrityError:
    conn.rollback()
    print("Course ID or name already exists.")

def view_courses(conn):
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM courses")
  courses = cursor.fetchall()

  if courses:
    for course in courses:
      print(f"Course ID: {course[0]} || Course: {course[1]}")
  else:
    print("No courses added yet.")