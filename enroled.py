import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('enroled.db')
cursor = conn.cursor()

# Create the student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY
    )
''')

# Create the course table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS course (
        dept_id TEXT,
        course_id INTEGER,
        PRIMARY KEY (dept_id, course_id)
    )
''')

# Create the enrolled table with foreign keys
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrolled (
        dept_id TEXT,
        course_id INTEGER,
        student_id INTEGER,
        FOREIGN KEY (dept_id, course_id) REFERENCES course(dept_id, course_id),
        FOREIGN KEY (student_id) REFERENCES student(student_id)
    )
''')

# Insert unique student records
students = [
    (11,),
    (12,),
    (22,),
    (33,)
]

cursor.executemany('''
    INSERT OR IGNORE INTO student (student_id)
    VALUES (?)
''', students)

# Insert unique course records
courses = [
    ('CS', 101),
    ('Math', 101),
    ('CS', 201),
    ('Math', 201),
    ('EE', 102),
    ('Math', 301)
]

cursor.executemany('''
    INSERT OR IGNORE INTO course (dept_id, course_id)
    VALUES (?, ?)
''', courses)

# Insert enrolled data
enrolled_data = [
    ('CS', 101, 11),
    ('Math', 101, 11),
    ('CS', 101, 12),
    ('CS', 201, 22),
    ('Math', 201, 33),
    ('EE', 102, 33),
    ('Math', 301, 22)
]

cursor.executemany('''
    INSERT INTO enrolled (dept_id, course_id, student_id)
    VALUES (?, ?, ?)
''', enrolled_data)

# Commit the transactions
conn.commit()

# Close the connection
conn.close()

print("Database and tables created successfully, and data inserted.")
