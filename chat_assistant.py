import sqlite3

def get_employees_in_department(department_name):
    conn = sqlite3.connect('chat_assistant.db')
    cursor = conn.cursor()
    query = '''
    SELECT Name, Salary, Hire_Date FROM Employees
    WHERE Department = ?
    '''
    cursor.execute(query, (department_name,))
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
department = 'Sales'
employees = get_employees_in_department(department)
if employees:
    for emp in employees:
        print(f'Name: {emp[0]}, Salary: {emp[1]}, Hire Date: {emp[2]}')
else:
    print(f'No employees found in {department} department.')
