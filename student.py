import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Data to be inserted into the student table
students = [
    (11, 'Bush', 3.0),
    (12, 'Cruz', 3.2),
    (13, 'Clinton', 3.9),
    (22, 'Sanders', 3.0),
    (33, 'Trump', 3.8)
]

# Insert the data into the student table
cursor.executemany('''
    INSERT INTO student (student_id, name, gpa)
    VALUES (?, ?, ?)
''', students)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully into the student table!")
