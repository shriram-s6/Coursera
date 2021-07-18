import sqlite3

conn = sqlite3.connect('practise.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""
 	create table employees ( 
	firstName text,
	lastName text,
	email text,
	salary integer
	)
	""")
employee_detail = [ ('Test1', 'Tes', 'test1@gmail.com', 7000),
					('Test2', 'Tes2', 'test2@gmail.com', 15000),
					('Test3', 'Tes3', 'test3@gmail.com', 25000),
 ]
c.executemany("insert into employees values (?, ?, ?, ?)", employee_detail)

c.execute("""
	select * from employees
	""")
# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())
for row in c.fetchall():
	print(row)

conn.commit()

# close the connection

conn.close()
