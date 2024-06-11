import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('department.db')
cursor = conn.cursor()

# Create student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gpa REAL
)
''')

# Create dept table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dept (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dean TEXT,
    building TEXT,
    room INTEGER
)
''')

# Insert data into dept table
departments = [
    (1, 'Computer Science', 'Rubio', 'Ajax', 100),
    (2, 'Mathemagics', 'Carson', 'Acme', 300),
    (3, 'Electrical Engineering', 'Kasich', 'Ajax', 200),
    (4, 'Industrial Engineering', 'Cruz', None, 200),
    (5, 'Musicology', 'Costello', 'North', 100)
]

cursor.executemany('''
INSERT INTO dept (dept_id, name, dean, building, room)
VALUES (?, ?, ?, ?, ?)
''', departments)

# Commit the transaction
conn.commit()

# Fetch and print the data to verify
cursor.execute('SELECT * FROM dept')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
