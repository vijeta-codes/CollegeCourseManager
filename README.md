
# College Course Manager

A Python-based College Course Management System built using SQLite. It allows users to manage courses and student enrollments through a simple menu-driven interface.

## Features

- Add and view courses
- Add and view students
- Search students by name or ID
- Update student course enrollment
- Delete student records
- Input validation
- Duplicate record handling
- Foreign key constraints
- SQLite database integration

## Technologies Used

- Python
- SQLite
- SQL

## Project Structure

```text
CollegeCourseManager/
│
├── main.py
├── database.py
├── course.py
├── student.py
├── create_demo_db.py
├── demo_college.db
├── README.md
└── .gitignore
```

## Database Design

The project uses two relational tables:

### Courses

| Column | Description |
|---|---|
| course_id | Primary Key |
| course_name | Unique course name |

### Students

| Column | Description |
|---|---|
| id | Auto-increment Primary Key |
| name | Student name |
| course_id | Foreign Key referencing courses |

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/vijeta-codes/CollegeCourseManager.git
```

### 2. Navigate to the project directory

```bash
cd CollegeCourseManager
```

### 3. Run the application

```bash
python main.py
```

The application uses the included demo database containing fictional sample records.

## Sample Data

The demo database includes five courses:

- Python
- Java
- SQL
- Django
- Flask

It also includes five fictional students for testing.

## Future Improvements

- Add unit testing
- Improve error logging
- Add a graphical user interface
- Develop a web-based version

## Author

**Vijeta Mohanty**

GitHub: [@vijeta-codes](https://github.com/vijeta-codes)
