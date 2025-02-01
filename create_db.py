import sqlite3



# Create and connect to the SQLite database
conn = sqlite3.connect('chat_assistant.db')
cursor = conn.cursor()


# Delete existing rows to avoid duplication
cursor.execute('DELETE FROM Employees')
cursor.execute('DELETE FROM Departments')

# Create the Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date TEXT NOT NULL
)
''')

# Create the Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
)
''')

# Insert sample data into Employees table
cursor.executemany('''
INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
    (4, 'David', 'Sales', 55000, '2020-11-25'),
(5, 'Eve', 'Engineering', 75000, '2019-07-15'),
(6, 'Frank', 'Marketing', 65000, '2021-09-10'),
(7, 'Grace', 'Sales', 48000, '2022-01-12'),
(8, 'Hank', 'Engineering', 70000, '2020-03-22')
])

# Insert sample data into Departments table
cursor.executemany('''
INSERT INTO Departments (ID, Name, Manager)
VALUES (?, ?, ?)
''', [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie'),
    (4, 'HR', 'David'),
    (5, 'Finance', 'Eve')
])

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
