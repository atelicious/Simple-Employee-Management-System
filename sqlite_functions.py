import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (first text, last text, pay integer, position text, department text, supervisor text)""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay, :position, :department, :supervisor)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay, 'position':emp.position,
                    'department': emp.department, 'supervisor': emp.supervisor})

def get_emp_by_last_name(lastname):
    with conn:
        c.execute("SELECT * FROM employees WHERE last =:last ", {'last': lastname})
    return c.fetchall()

def get_emp_by_first_name(firstname):
    with conn:
        c.execute("SELECT * FROM employees WHERE first =:first ", {'first': firstname})
    return c.fetchall()

def show_all_emp():
    with conn:
        c.execute("SELECT * FROM employees ")
    return c.fetchall()

def search_employee(first, last):
    with conn:
        c.execute("SELECT * FROM employees WHERE first =:first AND last =:last ", {'first': first, 'last': last})
    return c.fetchone()

def update_pay(first, last, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND
                    last = :last""", {'first': first, 'last': last, 'pay': pay}
                )

def update_first(old, last, new):
    with conn:
        c.execute("SELECT * FROM employees WHERE first =:old AND last =:last ", {'old': old, 'last': last})
        c.execute("""UPDATE employees SET first = :new_first """, {'new_first': new})

def remove_emp(first, last):
    with conn:
        c.execute("DELETE from employees WHERE first = :first and LAST = :last", {'first':first,
            'last':last})