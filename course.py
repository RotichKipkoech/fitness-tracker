import sqlite3

# Connect to SQLite database (creates a new database file if it doesn't exist)
conn = sqlite3.connect('course.db')
cur = conn.cursor()

# Create dept table
cur.execute('''
CREATE TABLE IF NOT EXISTS dept (
    dept_id TEXT PRIMARY KEY
)
''')

# Create course table
cur.execute('''
CREATE TABLE IF NOT EXISTS course (
    dept_id TEXT,
    course_id INTEGER,
    name TEXT,
    hours INTEGER,
    PRIMARY KEY (dept_id, course_id),
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
)
''')

# Insert data into dept table
departments = [
    ('CS',),
    ('Math',),
    ('Music',),
    ('EE',),
    ('IE',)
]
cur.executemany('INSERT OR IGNORE INTO dept (dept_id) VALUES (?)', departments)

# Insert data into course table
courses = [
    ('CS', 101, 'Programming', 4),
    ('CS', 201, 'Algorithms', 3),
    ('CS', 202, 'Systems', 3),
    ('Math', 101, 'Algebra', 3),
    ('Math', 201, 'Calculus', 4),
    ('Math', 301, 'Analysis', 4),
    ('Music', 104, 'Jazz', 3),
    ('EE', 102, 'Circuits', 3),
    ('IE', 101, 'Probability', 3),
    ('IE', 102, 'Statistics', 3)
]
cur.executemany('''
INSERT OR IGNORE INTO course (dept_id, course_id, name, hours)
VALUES (?, ?, ?, ?)
''', courses)

# Commit the changes
conn.commit()

# Verify the data insertion
print("Departments:")
cur.execute('SELECT * FROM dept')
for row in cur.fetchall():
    print(row)

print("\nCourses:")
cur.execute('SELECT * FROM course')
for row in cur.fetchall():
    print(row)

# Close the connection
conn.close()
