from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('chat_assistant.db')
    conn.row_factory = sqlite3.Row
    return conn

def process_query(query):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to show employees in a department
    if "employees in the" in query and "department" in query:
        department = query.split("in the")[1].split("department")[0].strip()
        cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (department,))
        employees = cursor.fetchall()
        if employees:
            return f"Employees in the {department} department: " + ", ".join([emp['Name'] for emp in employees])
        else:
            return f"No employees found in the {department} department."
    
    # Query to find the manager of a department
    if "manager of the" in query and "department" in query:
        department = query.split("of the")[1].split("department")[0].strip()
        cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        manager = cursor.fetchone()
        if manager:
            return f"The manager of the {department} department is {manager['Manager']}."
        else:
            return f"No manager found for the {department} department."
    
    # Query to list employees hired after a specific date
    if "employees hired after" in query:
        date = query.split("after")[1].strip()
        cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        employees = cursor.fetchall()
        if employees:
            return f"Employees hired after {date}: " + ", ".join([emp['Name'] for emp in employees])
        else:
            return f"No employees found hired after {date}."
    
    # Query for total salary expense for a department
    if "salary expense for the" in query and "department" in query:
        department = query.split("for the")[1].split("department")[0].strip()
        cursor.execute("SELECT SUM(Salary) AS TotalSalary FROM Employees WHERE Department = ?", (department,))
        total_salary = cursor.fetchone()
        if total_salary and total_salary['TotalSalary']:
            return f"The total salary expense for the {department} department is {total_salary['TotalSalary']}."
        else:
            return f"No salary data found for the {department} department."
    
    # If the query doesn't match any of the above, return this message
    return "Sorry, I couldn't understand your query."

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        user_query = request.form['query']
        response = process_query(user_query)
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
