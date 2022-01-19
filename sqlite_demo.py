import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
  first text,
  last text,
  pay integer
)""")






def insert_emp(emp):
  with conn:
    c.execute("INSERT INTO employees VALUES (?,?,?)", (emp.first, emp.last, emp.pay))
  
def get_emps_by_lastname(lastname):
  with conn:
    c.execute("SELECT * FROM employees WHERE last=?", (lastname))
    return c.fetchall()

def update_emp_pay(emp, pay):
  with conn:
    c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
    {'first': emp.first, 'last': emp.last, 'pay': pay})
  
def remove_emp(emp):
  with conn:
    c.execute("DELETE from employees WHERE first = :first AND last = :last",
    {'first': emp.first, 'last': emp.last})

def get_all_emp():
  with conn:
    c.execute("SELECT * FROM employees")
    return c.fetchall()



emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

update_emp_pay(emp_1, 10000)
remove_emp(emp_1)

all_emps = get_all_emp()
print(all_emps)





# c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
#   {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()


# print(emp_1.first)



# c.execute("SELECT * FROM employees WHERE last='Schafer'")

# print(c.fetchone())

conn.commit()
conn.close()