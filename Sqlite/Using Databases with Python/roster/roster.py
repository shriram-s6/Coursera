import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
drop table if exists User;
drop table if exists Member;
drop table if exists Course;

create table User (
    id     integer not null primary key autoincrement unique,
    name   text unique
);

create table Course (
    id     integer not null primary key autoincrement unique,
    title  text unique
);

create table Member (
    user_id     integer,
    course_id   integer,
    role        integer,
    primary key (user_id, course_id)
)
''')

fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]
    # print((name, title))

    cur.execute('''insert or ignore into User (name)
        values ( ? )''', ( name, ) )
    cur.execute('select id from User where name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''insert or ignore into Course (title)
        values ( ? )''', ( title, ) )
    cur.execute('select id from Course where title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''insert or replace into Member
        (user_id, course_id, role) values ( ?, ?, ? )''',
        ( user_id, course_id, role, ) )

query = """
    select User.name,Course.title, Member.role from 
    User join Member join Course 
    on User.id = Member.user_id and Member.course_id = Course.id
    order by User.name desc, Course.title desc, Member.role desc limit 2;
"""
for row in cur.execute(query):
    print(row[0], row[1], row[2])

query = """
    select 'XYZZY' || hex(User.name || Course.title || Member.role ) as X from 
    User join Member join Course 
    on User.id = Member.user_id and Member.course_id = Course.id
    order by X limit 1;
"""
for row in cur.execute(query):
    print(row[0])

conn.commit()
cur.close()
