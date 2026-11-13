import sqlite3

def connect_db(db_name="college.db"):
  conn = sqlite3.connect(db_name)
  conn.execute("PRAGMA foreign_keys = ON")
  return conn 

def create_tables(conn):
  cursor = conn.cursor()

  cursor.execute("""
   CREATE TABLE IF NOT EXISTS courses(
   course_id INTEGER PRIMARY KEY,
   course_name TEXT NOT NULL UNIQUE
   )
  """)

  cursor.execute("""
   CREATE TABLE IF NOT EXISTS students(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   course_id INTEGER,
   FOREIGN KEY (course_id)
   REFERENCES courses(course_id)
   )
  """)
  conn.commit()
