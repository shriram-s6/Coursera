import sqlite3

# creating a database called ages
conn = sqlite3.connect('ages.db')

# opening the cursor
c = conn.cursor()

# creating a table called Ages
c.execute("""
	create table Ages ( 
		name VARCHAR(128), 
		age integer
	)
""")

# deleting the previous rows in the table if any
c.execute("""
	delete from Ages
	""")

conn.commit()

# inserting rows into the Ages table
c.execute("INSERT INTO Ages (name, age) VALUES ('Marina', 35)")
c.execute("INSERT INTO Ages (name, age) VALUES ('Anabelle', 13)")
c.execute("INSERT INTO Ages (name, age) VALUES ('Ceridwen', 39)")
c.execute("INSERT INTO Ages (name, age) VALUES ('Aulay', 24)")
c.execute("INSERT INTO Ages (name, age) VALUES ('Nathanael', 14)")

conn.commit()

# executing the below select query

c.execute("select hex(name || age) as X from Ages order by X")
# printing the first record
print(c.fetchone())				# 416E6162656C6C653133

conn.close()