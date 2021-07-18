import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('musicalDB.sqlite')

# create a cursor
c = conn.cursor()

# using executescript() to run multiple queries

c.executescript("""
	drop table  if exists Artist;
	drop table if exists Genre;
	drop table if exists Album;
	drop table if exists Track;

	CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
	""")

def lookup(d, key):
	present = None
	for child in d:
		if present: return child.text
		if child.tag == 'key' and child.text == key:
			present = True
	return None	

file_name = 'Library.xml'
tree = ET.parse(file_name)
dict_tags = tree.findall('dict/dict/dict')
print('Dict count: ', len(dict_tags))
for each_tag in dict_tags:
	if lookup(each_tag, 'Track ID') is None: continue

	track_name = lookup(each_tag, 'Name')
	artist_name = lookup(each_tag, 'Artist')
	album_name = lookup(each_tag, 'Album')
	genre = lookup(each_tag, 'Genre')
	count = lookup(each_tag, 'Play Count')
	rating = lookup(each_tag, 'Rating')
	length = lookup(each_tag, 'Total Time')

	if track_name is None or artist_name is None or album_name is None or genre is None:
		continue

	# inserting artist name into artist table and fetching artist id
	c.execute("""
		insert or ignore into Artist (name) values (?)""", (artist_name, ))
	c.execute("""
		select id from Artist where name = ?""", (artist_name,))
	artist_id = c.fetchone()[0]

	print(genre)
	# inserting genre name into Genre table and fetching genre id
	c.execute("""
		insert or ignore into Genre (name) values (?)""", (genre, ))
	c.execute("""
		select id from Genre where name = ?""", (genre, ))
	genre_id = c.fetchone()[0]

	# inserting album details into Album table and fetching album id
	c.execute("""
		insert or ignore into Album (title, artist_id) values (?, ?)""",
		(album_name, artist_id, ))
	c.execute("""
		select id from Album where title = ?""", (album_name, ))
	album_id = c.fetchone()[0]

	c.execute("""
		insert or replace into Track (title, album_id, genre_id, len, rating,  count)
		values (?, ?, ?, ?, ?, ?)""", 
		(track_name, album_id, genre_id, length, rating, count))

conn.commit()

query = """
	select Track.title, Artist.name, Album.title, Genre.name 
    from Track join Genre join Album join Artist 
    on Track.genre_id = Genre.ID and Track.album_id = Album.id 
    and Album.artist_id = Artist.id order by Artist.name limit 3
"""

for row in c.execute(query):
	print(row[0], row[1], row[2], row[3])

c.close()
