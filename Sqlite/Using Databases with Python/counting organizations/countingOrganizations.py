import sqlite3

# creating a database 
conn = sqlite3.connect('countOrg.sqlite')
c = conn.cursor()

c.execute("drop table if exists Counts")

# creating a table
c.execute("""
	CREATE TABLE Counts (org TEXT, count INTEGER)
	""")
conn.commit()

file_name = 'mbox.txt'

mbox = open(file_name)
for line in mbox:
	if not line.startswith('From: '): continue
	email = line.split()[1]
	index = email.index('@')
	domain = email[index + 1:]
	c.execute("select count from Counts where org = ?", (domain,))
	row = c.fetchone()

	if row is None:
		c.execute("""
			insert into Counts (org, count) values (?, 1)""", (domain,))
	else:
		c.execute("""
			update Counts set count = count + 1 where org = ?""", (domain,))

conn.commit()

query = "select org, count from Counts order by count desc limit 10"
for row in c.execute(query):
	print(row[0], row[1])

conn.close()
